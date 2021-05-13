import itertools

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
              #if (d[i][k] != float("INF")) and (d[k][j] != float("INF")):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
        #print(d)
    return d

N, M ,R = map(int, input().split())
r = list(map(int, input().split()))
rr = list(itertools.permutations(r, R))
ab = [[10 ** 10] * N for i in range(N)]
for i in range(N):
  ab[i][i] = 0
  
for i in range(M):
  a, b, c = list(map(int, input().split()))
  ab[a - 1][b - 1] = c
  ab[b - 1][a - 1] = c
  
ans = warshall_floyd(ab)  
#print(rr)
#print(ans)
#2 ** 8
answer = 10 ** 12
for i in rr:
  now = 0
  #print(i)
  for j in range(R - 1):
    now += ans[i[j] - 1][i[j + 1] - 1]
    
  answer = min(answer, now)  
  
print(answer)



    
    
    

