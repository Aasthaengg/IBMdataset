w,a,b=map(int,input().split())
if b>a+w:
  ans=b-(a+w)
elif a>b+w:
  ans=a-(b+w)
else:
  ans=0
  
print(ans)