N = int(input())
A = list(map(int, input().split()))
assert len(A) == N - 1
count = [0 for i in range(N)]
for a in A:
  count[a-1] += 1
for n in range(N):
  print(count[n])