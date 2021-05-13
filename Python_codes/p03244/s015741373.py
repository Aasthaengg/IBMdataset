"""
与えられた数列の奇数番目の数と偶数番目の数をそれぞれ確認し、
要素数の多いものにそれぞれ書き換える。
文字種が1種類にならないように注意する
"""
from collections import Counter

N = int(input())
V_LI = list(map(int, input().split()))
if len(set(V_LI)) == 1:
    # そもそも一種類しかなかったら
    print(N // 2)
    exit()
odd_li = [V_LI[i] for i in range(0, N, 2)]
even_li = [V_LI[i] for i in range(1, N, 2)]
odd_c = sorted(Counter(odd_li).items(), key=lambda x: -x[1])
even_c = sorted(Counter(even_li).items(), key=lambda x: -x[1])
if odd_c[0][0] == even_c[0][0]:
    cnt_1 = N
    cnt_2 = N
    # 偶数側を固定する
    if len(even_c) > 1:
        odd_cnt = len(odd_li) - odd_c[0][1]
        even_cnt = len(even_li) - even_c[1][1]
        cnt_1 = odd_cnt + even_cnt

    # 奇数側を固定する
    if len(odd_c) > 1:
        odd_cnt = len(odd_li) - odd_c[1][1]
        even_cnt = len(even_li) - even_c[0][1]
        cnt_2 = odd_cnt + even_cnt

    print(min(cnt_1, cnt_2))
else:
    odd_cnt = len(odd_li) - odd_c[0][1]
    even_cnt = len(even_li) - even_c[0][1]
    print(odd_cnt + even_cnt)
