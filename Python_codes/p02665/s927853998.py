# 深さdの上限を先に決める
N = int(input())
# Aは，葉として残す必要があるものの数
A = list(map(int, input().split()))

# 深さdのノード数の上限
limit = [1]
for i in range(1, N+1):
    if i == N:  # 一番深いところの上限はA[N]
        limit.append(A[i])
    else:
        limit.append((limit[-1]-A[i-1])*2)
        if limit[-1] < 0:
            print(-1)
            exit()

# Nが0の時の処理
if N == 0:
    if A[0] != 1:
        print(-1)
        exit()

# 一番深いところから構築して最後にsumをとる
ans = [A[-1]]
now_leaf = A[-1]  # 一番深いところから構築しており，今現在の葉の数
for i in range(N-1, -1, -1):
    # print(A[i])
    ans.append(min(now_leaf+A[i], limit[i]))
    now_leaf = ans[-1]
# 構築したものに対してジャッジする, 葉を確保できているかどうか
for i in range(N):
    # ans[N-i]とすることで，今は一番浅いところから見ている
    if (ans[N-i]-A[i])*2 < A[i+1]:  # 葉が確保できているか
        print(-1)
        exit()
print(sum(ans))
