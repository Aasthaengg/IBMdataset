n = int(input())
a = map(int, input().split())
for i in range(n-1):
  a = sorted(a)
  b = a.pop(0)
  c = a.pop(0)
  a.append((b+c)/2)
print(a[0])