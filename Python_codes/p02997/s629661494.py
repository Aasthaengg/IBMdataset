from itertools import combinations
N,K=map(int, input().split())
M=(N-1)*(N-2)//2
if K>M:
    print(-1)
else:
    E=[]
    for i in range(2,N+1):
        E.append((1,i))
    E+=list(combinations(range(2,N+1), 2))[:M-K]
    print(len(E))
    for e in E:
        print(*e)