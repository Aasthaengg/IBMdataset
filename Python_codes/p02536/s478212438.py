N,M=map(int,input().split())
city=[0]*(N+10)

#都市情報を初期化
for i in range(1,N+1):
  city[i]=i
  
#都市番号の小さい方を根としてUnionFind木を作成(大きい方を書き換える)
for i in range(M):
  A,B=map(int,input().split())
#  print(A,B)

#ルートチェック
  if city[A]!=A:
    root=city[A]
    while city[root]!=root:
      root=city[root]
    city[A]=root
  
  if city[B]!=B:
    root=city[B]
    while city[root]!=root:
      root=city[root]
    city[B]=root

#結合
  if city[A]!=city[B]:
    city[city[B]]=city[A]
    
#print(city)
  
#木が何種類あるかチェック
ck=[0]*(N+10)
for i in range(1,N+1):
  if city[i]!=i:
    root=city[i]
    while city[root]!=root:
      root=city[root]
    city[i]=root
    
  if ck[city[i]]==0:
    ck[city[i]]=1
    
#print(city)
#print(ck)
Ans=sum(ck)-1 #木の数-1=必要な道路数

print(Ans)