n,m= map(int, input().split())
vs = [0] * (n + 1)
for _ in range(m):
    a,b= map(int, input().split())
    vs[a] += 1
    vs[b] += 1
ans = "YES"
for i in range(n + 1):
    if vs[i] % 2 == 1:
        ans = "NO"
print(ans)