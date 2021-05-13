a,b=map(int,input().split())
i=min(a,b)
j=max(a,b)
while not(i==0) and not(j==0):
  x=i
  i=j%i
  j=x
print(int(a*b/j))