n,k=map(int,input().split())
candle=list(map(int,input().split()))
ans=2000000000
for i in range(n-k+1):
  if candle[i]<0 and candle[i+k-1]>0:
    temp=min(abs(candle[i]), candle[i+k-1])*2+max(abs(candle[i]), candle[i+k-1])
  elif candle[i+k-1]<=0:
    temp=abs(candle[i])
  elif candle[i]>=0:
    temp=candle[i+k-1]
  ans=min(temp, ans)
print(ans)