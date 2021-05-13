n = int(input())
k = int(input())
x = list(map(int, input().split()))

s = 0
for i in x:
  if abs(i - k) < i:
    i = abs(i - k)
  s += i * 2

print(s)