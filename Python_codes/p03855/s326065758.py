N, K, L = map(int,input().split())
 
road = [i for i in range(N)]
rail = [i for i in range(N)]
rank = [0 for i in range(N)]
 
def find(a, U):
  if a == U[a]:
    return a
  else:
    par = find(U[a], U)
    U[a] = par
    return par
  
for i in range(K):
  p, q = map(int,input().split())
  p -= 1
  q -= 1  
  a = find(p, road)
  b = find(q, road)
 
  road[a] = b
  
for i in range(L):
  p, q = map(int,input().split())
  p -= 1
  q -= 1  
  a = find(p, rail)
  b = find(q, rail)
 
  rail[a] = b
  
for i in range(N):
  #print(road, rail)
  road[i] = find(road[i],road)
  rail[i] = find(rail[i],rail)
  
rr = [(road[i], rail[i]) for i in range(N)]
D = {}
for r in rr:
  if not r in D:
    D[r] = 1
  else:
    D[r] += 1
#print(road,rail)
#print(D)
 
for i in range(N):
  print(D[(road[i],rail[i])])