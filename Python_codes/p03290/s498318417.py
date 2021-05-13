D,G=map(int,input().split())
# bit全探索で、全問解く問題の組み合わせをすべて試す
 
scores=[None]*D
for i in range(D):
  p,c=map(int,input().split())
  # 一問の得点、問題数、ボーナス、全てといたときの得点
  scores[i]=[(i+1)*100,p,c,((i+1)*100)*p+c]
 
# あとあとのために点数高い順に並べる
scores=sorted(scores,key=lambda x:x[0])[::-1]
 
# 全問とく組み合わせに対して、最小の問題数
ans=D*100
for i in range(2**D):
  total=0
  solve=0
  for j in range(D):
    if (i>>j)&1:
      # 全問とく問題のボーナスを足していく
      total+=scores[j][3]
      solve+=scores[j][1]
  if total>=G:
    if ans>solve:
      ans=solve
    continue
  rest=G-total
  for j in range(D):
    if (i>>j)&1==0:
      point=scores[j][0]
      num=scores[j][1]-1 # 全問とかないので1減らす
      if point*num<rest:
        rest-=point*num
        solve+=num
      else:
        solve+=(rest//point+(rest%point>0))
        rest=0
    if rest<=0 and ans>solve:
      ans=solve
  
print(ans)