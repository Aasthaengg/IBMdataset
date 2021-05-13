#18:29
n = int(input())
mod = 10 ** 9 + 7
now = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
now[3][3][3] = 1
#print(part)
boo = [[0,0,1,2],[1,0,1,2],[2,0,1,2],[3,0,1,2],
       [0,0,1,2],[0,1,1,2],[0,2,1,2],[0,3,1,2],
       [0,1,0,2],[0,1,1,2],[0,1,2,2],[0,1,3,2],
       [0,1,0,2],[1,1,0,2],[2,1,0,2],[3,1,0,2],
       [0,0,2,1],[1,0,2,1],[2,0,2,1],[3,0,2,1]]
#print(now)
for i in range(n):
  last = now
  now = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
  #print(i,'l',last)
  #print(i,'n',now)
  for i in range(4):
    for j in range(4):
      for k in range(4):
        for l in range(4):
          if [i,j,k,l] not in boo:
            now[j][k][l] += last[i][j][k]
            now[j][k][l] %= mod
ans = 0
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans += now[i][j][k]
      ans %= mod
#print(last)
#print(now)
print(ans)