N,M = map(int, input().split())
data = list(map(int, input().split()))
S = 0
for i in range(0,len(data)):
    S += data[i]

if N >= S:
    print(N - S)
else:
    print(-1)