n,c=map(int,input().split())
bangumi=[tuple(map(int,input().split())) for i in range(n)]
jikan=[0]*(10**5+1)

#チャンネルごとにソート
from operator import itemgetter
bangumi=sorted(bangumi, key=itemgetter(2,0))

nowch=0
syuryo=0
for s,t,c in bangumi:
  if c==nowch and s==syuryo:
    for i in range(s+1,t+1): #時刻Sでの重複数え上げを防ぐ
      jikan[i]+=1
  else:
    for i in range(s,t+1):
      jikan[i]+=1
  nowch=c
  syuryo=t

#print(bangumi)
print(max(jikan))