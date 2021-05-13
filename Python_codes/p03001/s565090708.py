a,b,c,d=map(int,input().split())
x=0
if a/2==c and b/2==d:
  x=1
s=str((a*b)/2)+" "+str(x)
print(s)