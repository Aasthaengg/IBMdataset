N,M = map(int,input().split())
rs = [0]*N
for i in range(M):
    a, b = map(int, input().split())
    rs[a-1]+=1
    rs[b - 1] += 1
for r in rs:
    print(r)
