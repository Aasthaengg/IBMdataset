n = int(input())
a = list(map(int, input().split()))

x = 0
for i in a:
  x ^= i
print(*list(x^i for i in a))