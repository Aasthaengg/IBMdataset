W,a,b=map(int,input().split())
ans=0
if a<b and a+W<b:
  ans=b-(W+a)
elif a>b and b+W<a:
  ans=a-(W+b)
print(ans)
