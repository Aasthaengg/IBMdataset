N, M = map(int, input().split())
ans = [0]*M

for _ in range(N):
  K, *A = map(int, input().split())
  for x in A:
    ans[x-1] += 1

print(sum([1 for i in ans if i == N]))