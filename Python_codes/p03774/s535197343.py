N, M = list(map(int, input().split()))
P, CP = [], []

for i in range(N):
    P.append(list(map(int, input().split())))
for i in range(M):
    CP.append(list(map(int, input().split())))

for i in range(N):
    a, b = P[i][0], P[i][1]
    now = 10**10
    for j in reversed(range(M)):
        c, d = CP[j][0], CP[j][1]
        distance = abs(a-c)+abs(b-d)
        if distance <= now:
            result = j+1
            now = distance
    print(result)