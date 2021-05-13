N,K = map(int,input().split())

cnt = 0
d = []
for _ in range(N):
    a,b = map(int,input().split())
    d.append((a,b))

for i,j in sorted(d):
    cnt += j
    if cnt >= K:
        print(i)
        break