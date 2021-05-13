n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=sum(b)-sum(a)
for i,j in zip(a,b):
  if i<j:cnt-=(j-i+1)//2
print(['No','Yes'][cnt>=0])