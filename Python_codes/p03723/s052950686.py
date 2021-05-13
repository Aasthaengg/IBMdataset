a,b,c = tuple(map(int,input().split()))

ans = 0
while True:
  if len(set((a,b,c)))==1:
    if a%2==1:
      print(0)
      exit()
    print(-1)
    exit()
  if a%2==0 and b%2==0 and c%2==0:
    a,b,c = b//2+c//2,c//2+a//2,a//2+b//2
    ans+=1
  else:
    break
print(ans)