n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mx=0
for i in range(n):
  ans=sum(x[:i+1])+sum(y[i:])
  if ans>mx:
    mx=ans

print(mx)