N, K = map(int, input().split())
Sunuke = [0]*N
for _ in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for a in A:
    Sunuke[a-1] += 1

ans = 0
for s in Sunuke:
  if s == 0:
     ans += 1
print(ans)
