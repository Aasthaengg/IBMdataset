from bisect import bisect_left, bisect_right

N = int(input())

# 二分探索するためにソートしておく
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    # Bから一つ選ぶ
    b = B[i]
    # bisect_left(ソート済リスト、挿入したい値)
    # leftなので既に値が存在ししていたら既存の左に挿入
    a_ix = bisect_left(A, b)
    # rightも同様
    c_ix = bisect_right(C, b)
    # ex. A = [1, 3, 5], C = [2, 4, 6], b = 5の場合
    # a_ix=2（1と3が可能）, c_ix=2（6が可能）
    # c_ixについては　(全体-ダメな場合の個数)=OKな個数
    ans += a_ix * (N - c_ix)

print(ans)
