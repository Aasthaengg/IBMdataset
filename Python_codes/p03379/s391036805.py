n=int(input())
x=[int(x) for x in input().split()]
x1=sorted(x)

left=x1[n//2-1]
right=x1[n//2]

for i in x:
  if i<=left:
    print(right)
  else:
    print(left)