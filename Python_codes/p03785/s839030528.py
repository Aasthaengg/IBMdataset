n,c,k = map(int,input().split())
t = []

for i in range(n):
    t.append(int(input()))

t = sorted(t)
i = 1
machi = k
nori = 1
ans = 1

while i != n:
    if  machi-(t[i]-t[i-1]) >= 0 and nori+1 <= c:
        machi -= (t[i]-t[i-1])
        nori += 1
    else:
        ans += 1
        machi = k
        nori = 1
    i += 1

print(ans)
