n=int(input())
a=[int(input()) for i in range(n)]
b=sorted(a)
m=b[-1]
c=b[-2]
for i in range(0, n):
  if m == a[i]:
    print(c)
  else:
    print(m)
