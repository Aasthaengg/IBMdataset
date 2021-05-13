N,K=map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(N)]
ab.sort()
tmp = 0
for a, b in ab:
    tmp += b
    if tmp >= K:
        print(a)
        break
