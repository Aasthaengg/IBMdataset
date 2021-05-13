h,a=map(int,input().split())
ans=h//a+1
if h%a==0:
  ans-=1
print(ans)
