n,m,x=map(int,input().split())
n=[*range(1,n+1)];maxN=max(n)
a=list(map(int,input().split()))
count1,count2=0,0
for i in range(x,maxN+1):
  if i in a:
    count1+=1
for i in range(x,0,-1):
  if i in a:
    count2+=1
print(min(count1,count2))