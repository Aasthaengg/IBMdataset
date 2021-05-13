n=int(input())
a=list(map(int,input().split()))
x=0
cnt=0
sum=0
for i in a:
  if x==0:
    x=i
  elif i<=x:
    cnt+=1
    sum=max(sum,cnt)
    x=i
  else:
    cnt=0
    x=i
print(sum)