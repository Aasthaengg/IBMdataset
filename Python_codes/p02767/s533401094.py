n=int(input())
x=list(map(int,input().split()))
mi=min(x)
ma=max(x)
ans = sum(x)**2
for i in range (mi,ma+1):
  hp=0
  for j in x:
    hp+= (i-j)**2
  ans = min(hp,ans)
print(ans)
