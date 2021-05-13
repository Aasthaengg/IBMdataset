# ABC 116 D

import heapq

def resolve():
    n, k = map(int, input().split())
    td = []

    # td に score が高い順に格納する
    for _ in range(n):
        t, d = map(int, input().split())
        heapq.heappush(td, (-d, t))

    score = 0
    types = set()
    discard = []

    for _ in range(k):
        d, t = heapq.heappop(td)  # 注意 d は符号が逆になってる
        score -= d
        if t not in types:
            types.add(t)
        else:
            # その type で1番じゃないものをスコアの小さい順に並べる -> 後で捨てるリスト
            heapq.heappush(discard, (-d, t))

    ans = score + len(types)**2

    while td and discard:
        d, t = heapq.heappop(td)  # 残り物からスコア高い順に取り出す; 注意 このリストのスコアは符号反転してる

        if t in types:
            # 選んでも種類が増えないやつはパス
            continue

        types.add(t)
        score -= d

        # 捨てても種類が減らないリストの中で最もスコアが低いやつを捨てる
        _d, _t = heapq.heappop(discard)  # 注意 このリストのスコアは符号反転していない
        score -= _d

        ans = max(ans, score + len(types)**2)

    print(ans)

if __name__ == "__main__":
    resolve()
