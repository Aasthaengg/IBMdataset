n = int(input())
res = 0
for i in range(n):
  a,b = map(str, input().split())
  if b == 'JPY':
    res += float(a)
  else:
    res += float(a) * 380000.0
print(res)