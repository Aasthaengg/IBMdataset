a,b,c=map(int,input().split())
d=list(map(int,input().split()))
result1=list(range(0,c+1))
result2=list(range(c,a+1))
ans1=0
ans2=0
for i in result1:
  if i in d:
    ans1+=1
for i in result2:
  if i in d:
    ans2+=1
print(min(ans1,ans2))