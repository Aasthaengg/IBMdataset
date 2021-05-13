s = input()
k = int(input())
n = len(s)

if len(set(s)) == 1:
    print(n*k//2)
    exit()

ss = s + s
cnts = 0
now = s[0]
temp = 1
for i in range(1, n):
    if s[i] == now:
        temp += 1
    else:
        cnts += temp // 2
        temp = 1
        now = s[i]
cnts += temp // 2

cntss = 0
now = ss[0]
temp = 1
for i in range(1, 2*n):
    if ss[i] == now:
        temp += 1
    else:
        cntss += temp // 2
        temp = 1
        now = ss[i]
cntss += temp // 2

kousa = cntss - cnts
print(cnts + kousa*(k-1))