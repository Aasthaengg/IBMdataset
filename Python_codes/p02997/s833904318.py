"""
まず、最短距離が2であるような点の組み合わせの数が最も多くなるように木を作る。
そのあと、最短距離が2であるような点の組み合わせの数がKになるまで、辺を増やしていく。
"""

N,K = map(int,input().split())

if K > (N-1)*(N-2)//2:
    print(-1)
    exit()

ans = []
for i in range(1,N):
    ans.append((str(i),str(N)))

cnt = (N-1)*(N-2)//2
for i in range(1,N):
    for j in range(i+1,N):
        if cnt == K:
            break
        ans.append((str(i),str(j)))
        cnt -= 1
    else:
        continue
    break
print(len(ans))
for a in ans:
    print(" ".join(a))