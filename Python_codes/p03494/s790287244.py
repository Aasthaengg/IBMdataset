n=int(input())
l=list(map(int,input().split()))

ans=0
while True:
  for i in l:
    if i%2!=0:
      print(ans)
      exit()
  ans+=1
  l=[i/2 for i in l]
