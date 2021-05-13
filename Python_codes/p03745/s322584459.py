n=int(input())
a=list(map(int,input().split()))
c=1
g=0
for i in range(n-1):
  if (g==1 and a[i+1]<a[i]) or (g==-1 and a[i+1]>a[i]) :
    c+=1
    g=0
  elif g==0:
    if a[i+1]>a[i]:
      g=1
    elif a[i+1]<a[i]:
      g=-1
print(c)