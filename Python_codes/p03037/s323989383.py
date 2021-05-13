n,m = map(int,input().split())
k = [list(map(int,input().split())) for i in range(m)]
l,r = [list(i) for i in zip(*k)]

x = max(l)
y = min(r)

p = 0
for i in range(1,n+1):
    if x <= i and i <= y:
        p += 1

print(p)