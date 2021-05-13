N=int(input())
b=list(map(int, input().split()))
a=[]

def f(b):
  i=len(b)-1
  while i>=0 and b[i]!=i+1:
    i-=1
  if i>=0:
    del b[i]
    return i, b
  else:
    return -1, []

j, b_=f(b)
while j>=0:
  a=[j]+a
  j, b_=f(b_)
  
if len(a)==N:
  for i in range(N):
    print(a[i]+1)
else:
  print(-1)