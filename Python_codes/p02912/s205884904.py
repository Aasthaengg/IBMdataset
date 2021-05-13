#　解説確認後AC
#　問題解説参考サイト 「けんちょんの競プロ精進記録」 より
#  URL: https://drken1215.hatenablog.com/entry/2019/09/16/032000
#　優先度付きキュー 参考記事　「【Python】優先度付きキューの使い方【heapq】」
#　URL: https://qiita.com/ell/items/fe52a9eb9499b7060ed6

import heapq

N,M = map(int,input().split())
a = list(map(int,input().split()))
a = list(map(lambda x: x*(-1), a)) # リストの要素を全てマイナス(最大値を取り出すため)
heapq.heapify(a) # 優先度付きキューへ
for _ in range(M):
    heapq.heappush(a,((heapq.heappop(a)*(-1))//2)*(-1)) # リストの最大値を取り出して割る2して挿入
print(abs(sum(a))) # abs()してマイナスを取り除く
