n = int(input())
a = list(map(int, input().split()))

x = 1

for num in a:
  if num%2 == 0:
    x *= 2
  else:
    x *= 1

print(3**n - x)