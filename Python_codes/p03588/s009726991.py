N = int(input())
max_a = 1
max_v = -1
for _ in range(N):
  a, b = [int(i) for i in input().split()]
  if max_a <= a:
    max_a = a
    max_v = b
print(max_a + max_v)
