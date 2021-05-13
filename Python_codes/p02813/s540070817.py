import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i, lis in enumerate(itertools.permutations([i for i in range(1, N + 1)])):
  lis = list(lis)
  if lis == P:
    a = i
  if lis == Q:
    b = i

print(abs(a - b))
