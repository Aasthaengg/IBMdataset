n=int(input())
a=list(input().split())
if n%2==0:  
  b=a[::2]
  a.pop(0)
  c=a[::2]
  c.reverse()
  print(' '.join(c+b))
else:
  b=a[::2]
  a.pop(0)
  c=a[::2]
  b.reverse()
  print(' '.join(b+c))