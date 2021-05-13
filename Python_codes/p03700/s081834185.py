n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]
l=0;r=max(h)//b+1
while abs(l-r)>1:
  x=(l+r)//2
  ct=0
  for i in range(n):
    ct+=((a-b-1)+max(0,h[i]-b*x))//(a-b)
  if ct<=x:
    r=x
  else:
    l=x
print(r)