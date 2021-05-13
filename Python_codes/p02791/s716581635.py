N = int(input())
P = list(map(int, input().split()))

MIN = 20000000
cnt = 0
for n in range(len(P)):
    if MIN > P[n]:
        cnt += 1
        MIN = P[n]

print(cnt)