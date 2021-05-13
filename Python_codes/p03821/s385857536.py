N = int(input())
a = []
b = []
for _ in range(N):
    ai,bi = list(map(int,input().split()))
    a.append(ai)
    b.append(bi)
ans = 0
for i in range(N-1,-1,-1):
    a[i] += ans
    t = (b[i] - a[i] ) % b[i]
    ans += t
print(ans)