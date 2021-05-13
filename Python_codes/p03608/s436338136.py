import itertools
import math

n , m , r = map(int , input().split())
rr = list(map(int,input().split()))
q = len(rr)
INF = 1145141919810364364334

p = list(itertools.permutations(rr))

d = [[INF] * n for _ in range(n)]

for i in range(n):
    d[i][i] = 0
    
for i in range(m):
    a,b,c = map(int , input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min( d[i][j] , d[i][k] + d[k][j] )
            
ans = INF
for i in p:
    temp = 0
    for j in range(q-1):
        temp += d[i[j] - 1][i[j+1] - 1]
        
    ans = min(ans , temp)
    
print(ans)