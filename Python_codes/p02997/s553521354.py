"""
最短距離が2であるようなノードの組み合わせは、最高で(N-1)C2個存在する。
そこで、この(N-1)C2個の組み合わせがある状態をデフォルトとして、K個になるまで辺を増やしていく。
"""

N,K = map(int,input().split())
if K > (N-1)*(N-2)//2:
    print(-1)
    exit()

edges = []
for i in range(2,N+1):
    edges.append((str(1),str(i)))

rest = (N-1)*(N-2)//2 - K
for i in range(2,N+1):
    for j in range(i+1,N+1):
        if rest == 0:
            break
        else:
            edges.append((str(i),str(j)))
            rest -= 1
    else:
        continue
    break
print(len(edges))
for edge in edges:
    print(" ".join(edge))
