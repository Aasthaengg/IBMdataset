N = int(input())
A = list(map(int, input().split()))
x = 1
for a in A:
  if a % 2 == 0:
    x *= 2
print(3 ** N - x)