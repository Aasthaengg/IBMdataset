import itertools

N, C = map(int, input().split())
D = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(N)]

cost = [[0 for _ in range(C)] for _ in range(3)]
#print(cost)

for cc in range(C):
  for i in range(N):
    for j in range(N):
      cost[(i+j)%3][cc] += D[c[i][j]-1][cc]
#print(cost)

answer = []
comb =[i for i in range(C)]
for v in itertools.permutations(comb, 3):
  answer.append(sum([cost[j][v[j]] for j in range(3)]))
print(min(answer))