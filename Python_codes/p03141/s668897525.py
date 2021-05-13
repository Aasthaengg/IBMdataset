n = int(input())
a = []
b = []
for i in range(n):
    t1,t2 = map(int,input().split())
    a.append(t1)
    b.append(t2)
wa = []
for i in range(n):
    wa.append(a[i] + b[i])
c = zip(wa,a,b)
c = sorted(c, reverse = True)
wa, a, b = zip(*c)
ans = 0
flg = 0
for i in range(n):
    if flg == 0:
        ans +=a[i]
        flg = 1
    else:
        ans -=b[i]
        flg = 0
print(ans)