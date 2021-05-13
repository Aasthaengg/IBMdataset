n,l=map(int,input().split())
if l <= 0 and l+n-1 >= 0:
  ate=0
elif l > 0:
  ate=l
else: # l+n-1 < 0
  ate=l+n-1
  
print((l-1)*n+n*(n+1)//2-ate)