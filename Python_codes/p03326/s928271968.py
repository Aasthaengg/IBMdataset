N,M=map(int,input().split())
cakes = [[int(i) for i in input().split()] for N in range(N)]
if M==0:
  print(0)
  quit()
#最大値、最初値計算
score=[0]*8
s=sorted(map(lambda c: c[0]+c[1]+c[2], cakes))
score[0]=sum(s[-M:])
score[1]=-sum(s[:M])
s=sorted(map(lambda c: c[0]+c[1]-c[2], cakes))
score[2]=sum(s[-M:])
score[3]=-sum(s[:M])
s=sorted(map(lambda c: c[0]-c[1]+c[2], cakes))
score[4]=sum(s[-M:])
score[5]=-sum(s[:M])
s=sorted(map(lambda c: c[0]-c[1]-c[2], cakes))
score[6]=sum(s[-M:])
score[7]=-sum(s[:M])
print(max(score))