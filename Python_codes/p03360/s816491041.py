N = list(map(int, input().split()))
K = int(input())

for i in range(K):
  N = sorted(N)
  N[-1] *= 2

print(sum(N))