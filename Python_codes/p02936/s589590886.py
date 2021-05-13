import sys
sys.setrecursionlimit(10**6)
# 解法 累積和とdfsを使うと探索が減ってなんかうまくいく．
N,Q = map(int,input().split())
E=[[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b)
    E[b-1].append(a)
dic = {}
for _ in range(Q):
    p,x = map(int,input().split())
    if not p-1 in dic:
        dic[p-1] = x
        continue
    dic[p-1] += x

res = [0 for _ in range(N)]
def dfs(p,s,ans):
    global res
    # 終わり条件　最後まで行ったら，つまりE[k] = []になったら.
    # 再帰 累積和を計算して，自分がつながっているノードに接続している
    if s-1 in dic:
        ans += dic[s-1]

    res[s-1] = str(ans)
    if E[s-1] == [p]:
        return
    for e in E[s-1]:
        if e == p:
            continue
        dfs(s,e,ans)
dfs(1,1,0)
print(' '.join(res))



