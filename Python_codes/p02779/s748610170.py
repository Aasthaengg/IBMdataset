n=int(input())
a=[int(x) for x in input().split()]
b=set(a)
l=len(b)
if l==n:
  print("YES")
else:
  print("NO")