"""
Nの制約数の少なさてきに、全探索するのがよさそう。
とはいえ、ありうるすべてのグラフパターンを全探索したら、2**(N^2)かかる

N本目以降は、辺の数を増やせば増やすほど、有効なペアの数が減っていく。
逆にいうと、ペアの数を減らしたい場合は、N本目以降を追加する
"""
N,K = map(int,input().split())
if K > N*(N-1)//2-(N-1):
    print(-1)
    exit()
edges = []
base = 1
for i in range(base+1,N+1):
    edges.append(" ".join([str(base),str(i)]))

diff = (N-1)*(N-2)//2 - K
base = 2
while diff:
    for i in range(base+1,N+1):
        if diff == 0:
            break
        else:
            edges.append(" ".join([str(base),str(i)]))
            diff -= 1
    base += 1
print(len(edges))
for ans in edges:
    print(ans)

