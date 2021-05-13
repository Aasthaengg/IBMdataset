n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
c = b[n//2]
d = b[n//2-1]
for i in a:
  if i >= c:
    print(d)
  else:
    print(c)