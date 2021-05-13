n=int(input())
a=[int(input()) for i in range(n)]
c=sorted(a)
b=max(a)
for i in range(n):
  if a[i]==b:
    print(c[n-2])
  else:
    print(b)