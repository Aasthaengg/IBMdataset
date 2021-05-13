p = int(input())
day, a = map(int, input().split())
day = day - 1
for i in range(p):
  b = int(input())
  b = day // b
  a = a + b + 1
print(a)
