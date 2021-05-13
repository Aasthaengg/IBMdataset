N, M = map(int, input().split())

pairs = []
for i in range(M):
    pairs.append(list(map(int, input().split())))

for i in range(1,N+1):
    s = 0
    for pair in pairs:
        if i in pair:
            s += 1
    print(s)