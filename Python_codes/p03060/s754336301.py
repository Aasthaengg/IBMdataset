N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
S = [V[i]-C[i] for i in range(N)]
ans = 0
for s in S:
  if s > 0:
    ans += s
print(ans)
