import sys
N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for l, r, d in (map(int, input().split()) for _ in range(M)):
    adj[l-1].append((r-1, d))
    adj[r-1].append((l-1, -d))

visited = [0]*N
dist = [0]*N

for i in range(N):
    if visited[i]:  # 探索したことのある(つまり矛盾がなかった)場所なら次の場所へ
        continue
    visited[i] = 1  # 探索したフラグを立てる
    stack = [i]  # 探索候補へ追加
    vset = set()  # 今回(iのターンで)探索する場所のリスト(という名のセット)

    while stack:
        v = stack.pop()  # 今探索する場所をvとする
        vset.add(v)  # 探索する場所を追加する
        for dest, d in adj[v]:
            if visited[dest]:
                continue
            visited[dest] = 1  # 探索したフラグ立てる
            dist[dest] = dist[v] + d  # 今回の情報でとりあえず距離を設定
            stack.append(dest)

    for v in vset:  # 今回探索した場所それぞれについて
        for dest, d in adj[v]:
            if dist[v] + d != dist[dest]:  # ほかの情報と矛盾するか
                print('No')  # 矛盾してたらNoとなる
                exit()

print('Yes')
