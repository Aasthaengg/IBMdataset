H,W,D = map(int,input().split())
A = [[]]
for i in range(H):
  A.append([0]+list(map(int,input().split())))
la = [[] for o in range(H*W+1)]
for i in range(1,H+1):
  for j in range(1,W+1):
    la[A[i][j]].append(i)
    la[A[i][j]].append(j)
Q = int(input())
q = []
for i in range(Q):
  q.append(list(map(int,input().split())))

l = [[0]+[0 for i in range((H*W-j)//D)] for j in range(D)]
#あまり0は特別扱い
i = 0
v = l[i]
for j in range(1,len(l[0])-1):
  mae = i + D*j
  ato = i + D*(j+1)
  v[j+1] = v[j] + abs(la[mae][0]-la[ato][0]) + abs(la[mae][1]-la[ato][1])
#あまり1~D-1まで
for i in range(1,D):
  v = l[i]
  for j in range(len(v)-1):
    mae = i + D*j
    ato = i + D*(j+1)
    v[j+1] = v[j] + abs(la[mae][0]-la[ato][0]) + abs(la[mae][1]-la[ato][1])

for i in range(Q):
  L,R = q[i][0],q[i][1]
  amari = L%D
  haji = (L-amari)//D
  owari = (R-amari)//D  
  print(l[amari][owari]-l[amari][haji])