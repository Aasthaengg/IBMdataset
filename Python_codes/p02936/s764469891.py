import sys
input = sys.stdin.readline

n,q = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(n-1)]
PX = [tuple(map(int, input().split())) for i in range(q)]
#print(AB)

C = [[] for i in range(n)] #Cはグラフ表示
for a,b in AB:
  C[b-1].append(a-1)
  C[a-1].append(b-1)
Q = [0] * n
for p,x in PX:
  Q[p-1] += x
#print(Q)
  
STACK = [0]
VISITED = [0] * n
ANS = [0] * n
ANS[0] = Q[0]
VISITED[0] = 1

while STACK:
  d = STACK.pop()
  for i in C[d]:
    if VISITED[i]:
      continue
    else:
      VISITED[i] = 1
      ANS[i] = ANS[d] + Q[i]
      STACK.append(i)

print(*ANS)