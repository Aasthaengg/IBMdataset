a,b=map(int,input().split())
ans=0
if a>=13:
  ans=b
elif 6<=a and a<=12:
  ans=b//2
print(ans)