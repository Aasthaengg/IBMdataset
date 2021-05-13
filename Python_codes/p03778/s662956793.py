W,a,b=map(int,input().split())
ans1=0
ans2=0
if b>(a+W):
  ans1=b-(a+W)
if a>(b+W):
  ans2=a-(b+W)
ans=max(ans1,ans2)
print(ans)