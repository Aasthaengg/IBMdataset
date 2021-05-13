N,M = (int(T) for T in input().split())
Road = []
for TM in range(0,M):
    Road.extend([int(T) for T in input().split()])
for TN in range(1,N+1):
    print(Road.count(TN))