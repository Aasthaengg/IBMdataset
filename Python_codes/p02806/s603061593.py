n = int(input())
dat = []
for i in range(n):
    t = input().split()
    dat.append((t[0], int(t[1])))
m = input()
f = False
res = 0
for i in range(n):
    if f:
        res += dat[i][1]
    else:
        if m == dat[i][0]:
            f = True
print(res)
