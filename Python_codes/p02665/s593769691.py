# 深さdの現実的な上限を先に決める
N = int(input())
# Aは，葉として残す必要があるものの数
A = list(map(int, input().split()))

# 深さdのノード数の上限
limit = [1]  # ルートのノードの上限数 : 当然1
for d in range(1, N+1):
    if d == N:  # 1番深いところの上限はA[N]
        limit.append(A[d])
    else:
        limit.append((limit[-1]-A[d-1])*2)
        # limit[-1] < A[d-1]の場合，葉を確保することができていない
        if limit[-1] < 0:
            print(-1)
            exit()

# Nが0の時の処理
if N == 0:
    if A[0] != 1:
        print(-1)
        exit()

# 1番深いところから構築して最後にsumを取る
ans = [limit[-1]]
# 1番深いところから構築しており，今現在のオードの数
now_node = limit[-1]
for d in range(N-1, -1, -1):
    # limitは深さが浅いところから押さえつけながら構築したと考える
    ans.append(min(now_node+A[d], limit[d]))  # now_nodeは深さd+1のノードの数, 今は深さdの部分の構築をしている
    now_node = ans[-1]  # 現在のノードの数

# 構築したものに対してジャッジする
ans.reverse()
for d in range(N):
    if (ans[d]-A[d])*2 < A[d+1]:  # 1つ深い部分の葉を構築するだけの労力を確保できているかどうか
        print(-1)
        exit()
print(sum(ans))
