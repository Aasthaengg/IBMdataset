N,M = map(int,input().split())
ab = []
for _ in range(M):
    ab.extend(list(map(int,(input().split()))))

for j in range(1,N+1):
    print(ab.count(j))