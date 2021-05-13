N,M = map(int, input().split())
L = [0]*(N+1)
for _ in range(M):
    a,b = map(int, input().split())
    L[a] += 1
    L[b] += 1

ans = "YES"
for l in L:
    if l%2 == 1:
        ans = "NO"
        break
print(ans)