N=int(input())
x=[list(map(int,input().split())) for _ in range(N)]
x.sort(key=lambda x:-x[2])
dp=[[0]*101 for i in range(101)]
bp=[[0]*101 for i in range(101)]
for j in range(101):
  for k in range(101):
    a,b,c=x[0]
    r=0
    asa=abs(a-j)+abs(b-k)+c
    for i in range(N):
      count=abs(x[i][0]-j)+abs(x[i][1]-k)
      if x[i][2]==max(asa-count,0):
        r+=1
    if r==N:
      print(j,k,asa)
      exit()