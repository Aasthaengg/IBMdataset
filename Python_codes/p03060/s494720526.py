N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
for i in range(N):
    V[i] = V[i]-C[i]
V.sort()
V.reverse()
ans = 0
for v in V:
    if v < 0:
        break
    ans += v
print(ans)