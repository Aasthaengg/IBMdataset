import sys
readline=sys.stdin.readline

DIV=10**9+7

N,K=map(int,readline().split())

E=[[] for i in range(N)]

for i in range(N-1):
  a,b=map(int,readline().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)
  
ans=1
stack=[]
# 頂点, 親, Kから引く数, Kから引く数のベースとなる数
stack.append([0,-1,0,0])
while stack:
  v,parent,minus,base=stack.pop()
  ans = (ans%DIV * (K-(minus+base))%DIV) % DIV
  if base < 2:
    base += 1
  cnt=0
  for child in E[v]:
    if child == parent:
      continue
    stack.append([child,v,cnt,base])
    cnt+=1
  
print(ans)  
  
  
