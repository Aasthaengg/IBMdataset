N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

fond = [0]*(M+1)

for i in A:
    for j in i[1:]:
        fond[j] += 1
        
print(fond.count(N))