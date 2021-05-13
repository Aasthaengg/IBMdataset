N = int(input())
E=[list(map(int,input().split())) for i in range(N-1)]
C=list(map(int,input().split()))
C.sort(reverse=True)

print(sum(C[1:]))

ELIST = [[] for i in range(N+1)]
for a,b in E:
  ELIST[a].append(b)
  ELIST[b].append(a)


from collections import deque
QUE =deque([1])

i=0
ANS=[-1]*(N+1)
while QUE:
  x=QUE.pop()
  ANS[x]=C[i]
  i+=1
  for to in ELIST[x]:
    if ANS[to]==-1: 
      QUE.append(to)
      ANS[to]=0
      
print(*ANS[1:])