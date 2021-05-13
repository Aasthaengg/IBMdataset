n,k,q=list(map(int,input().split()))
wins=[0]*n
for i in range(q):
  a=int(input())
  wins[a-1]+=1
#print(wins)

for w in wins:
  if k-(q-w)>0:
    print('Yes')
  else:
    print('No')