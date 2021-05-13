n=int(input())

ans=0
cnt=1
while n!=1:
  n//=2
  ans+=1*cnt
  cnt=cnt*2

ans+=1*cnt

print(ans)