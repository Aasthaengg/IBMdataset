n,k=map(int,input().split())
li=[list(map(int,input().split())) for i in range(n)]
gr=[0]*(n+1) #各グループの出現回数をメモする配列

from operator import itemgetter
li=sorted(li, key=itemgetter(1), reverse=True)

A=[] #大きい方からK個以内の配列で、2個以上あるやつの2番目以降のやつの大きさを記録

for i in range(k):
  if gr[li[i][0]]>=1:
    A.append(li[i][1])
  gr[li[i][0]]+=1

A.reverse()

B=[] #既に同じグループが登場してしまってない子の大きさを記録
for i in range(k,n):
  if gr[li[i][0]]==0:
    B.append(li[i][1])
  gr[li[i][0]]+=1

#現時点での種類数とポイントを測定
sp=set()
ans=0
for i in range(k):
  ans+=li[i][1]
  sp.add(li[i][0])
sp=len(sp)
ans+=sp*sp

koukan=[] #その交換で、累積でどの程度増減するか
zouka=0
for a,b in zip(A,B):
  zouka+=(sp+1)**2-sp**2-(a-b)
  #print(a,b,sp,zouka)
  koukan.append(zouka)
  sp+=1

#koukanの中で最大の増加を探して、ansに+する。
# print(A,B)
# print(koukan)
if koukan:
  ans+=max(0,max(koukan))

print(ans)