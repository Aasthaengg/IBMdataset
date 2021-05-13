s = input()
t = input()

n = len(s)
n = len(s)
a = [-1]*26
b = [-1]*26
flg = True

for i in range(n):
    snum = ord(s[i]) - 97
    tnum = ord(t[i]) - 97
    if a[snum] >= 0 and a[snum] != tnum:
        flg = False
        break
    if b[tnum] >= 0 and b[tnum] != snum:
        flg = False
        break
    if a[snum] == -1:
        a[snum] = tnum
    if b[tnum] == -1:
        b[tnum] = snum
    
print('Yes') if flg else print('No')