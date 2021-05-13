N = int(input())
A = list(map(int,input().split()))
ans = 0
p = {}
m = {}
for i in range(N):
    if p.get(i+A[i]) is None:
        p[i+A[i]] = 1
    else:
        p[i+A[i]] += 1
for i in range(N):
    if m.get(i-A[i]) is None:
        m[i-A[i]] = 1
    else:
        m[i-A[i]] += 1
for x in range(min(p),max(m)+1):
    if x in p and x in m:
        ans += p[x] * m[x]
print(ans)