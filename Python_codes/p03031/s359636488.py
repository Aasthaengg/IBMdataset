from itertools import combinations
n,m = map(int,input().split())
l = []
for i in range(m):
    u = list(map(int,input().split()))
    u = u[1:]
    l.append(u)

p = list(map(int,input().split()))
v = []
for i in range(1,n+1):
    v.append(i)

c = []
for i in range(n+1):
    a = combinations(v,i)
    for k in a:
        c.append(k)

ans = 0
for ele in c:
    s = set(ele)
    f = 0
    for i in range(len(l)):
        x = l[i]
        cnt = 0
        for j in x:
            if j in s:
                cnt = cnt+1

        if cnt%2 != p[i]:
            f = 1
            break

    if f == 0:
        ans = ans+1

print(ans)