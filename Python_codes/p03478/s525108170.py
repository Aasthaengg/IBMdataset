n, a, b = map(int, input().split())

f = 0
for i in range(1, n+1):
  s = sum(map(int, list(str(i))))
  if s >= a and s <= b:
    f += i
print(f)