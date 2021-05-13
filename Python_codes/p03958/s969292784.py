k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = a[-1]
b = sum(a[:-1])
if t == 1:
  print (k-1)
  exit()
print (max(0,s-b-1))