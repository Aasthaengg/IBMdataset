N = int(input())
K = int(input())
sum = 0
S = list(map(int, input().split()))
for i in range(N):
  x = S[i]
  if x >= K - x:
    sum += 2 * (K - x)
  else:
    sum += 2 * x
print(sum)