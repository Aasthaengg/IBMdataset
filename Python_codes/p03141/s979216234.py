N=int(input())

pablist=[]
for _ in range(N):
  A,B=map(int,input().split())  
  pablist.append((A+B,A,B))
pablist.sort()
#print(pablist)

tak_score=0
aok_score=0
turn=0
while pablist:
  p,a,b=pablist.pop()
  if turn&1==0:
    tak_score+=a
  else:
    aok_score+=b
  turn+=1
  
print(tak_score-aok_score)