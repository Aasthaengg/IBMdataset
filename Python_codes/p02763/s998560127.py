# 本当はBITやセグメントツリーを用いた解法を使いたいところ...(理解不足)

import bisect
from collections import defaultdict

N = int(input())
# 書き換える時に文字列だと不便なのでリスト化しておく
S = list(input())
Q = int(input())

# setは順序を保証しない、setで管理するとクエリ2で（リスト化した後に）ソートする必要がある
# 最初からlistで管理して、クエリ1ではソート済になるように挿入する
dict = defaultdict(list)
for i in range(N):
    dict[S[i]].append(i)

ans = []

for _ in range(Q):
    a, b, c = input().split()
    a = int(a)

    if a == 1:
        b = int(b) - 1
        # 書き換える必要がない場合
        if S[b] == c:
            continue
        else:
            # クエリ2が飛んできた時に毎回ソートしていては間に合わない
            # クエリ1の時点でソート済にしておく
            # 二分探索の際、同じ数字が既にあることはないので、leftでもrightでも良い
            dict[S[b]].remove(b)
            idx = bisect.bisect(dict[c], b)
            dict[c].insert(idx, b)
            # 文字列の書き換え
            S[b] = c

    elif a == 2:
        b = int(b) - 1
        c = int(c) - 1
        # 文字が何種類あるか
        char_cnt = 0
        for key, value in dict.items():
            # left,rightを指定する必要がある
            x1 = bisect.bisect_left(value, b)
            x2 = bisect.bisect_right(value, c)
            if x2 - x1 > 0:
                char_cnt += 1
        ans.append(char_cnt)

for i in ans:
    print(i)
