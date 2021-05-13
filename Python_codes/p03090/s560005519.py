import sys,math,collections,itertools
input = sys.stdin.readline
graph = []
cnt = 0

N=int(input())
if N%2 == 0:
    
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i+j == N+1:
                continue
            else:
                cnt+=1
                graph.append([i,j])
                
else:
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i + j == N:
                continue
            else:
                cnt+=1
                graph.append([i,j])
print(cnt)
for gr in graph:
    print(*gr)
                
