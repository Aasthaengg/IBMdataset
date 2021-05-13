N, M = map(int, input().split())
town = [0]*M*2
for i in range(M):
    town[i*2], town[i*2+1] = map(int, input().split())

for ans in range(1,N+1):
     print(town.count(ans))