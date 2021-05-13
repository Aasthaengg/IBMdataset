

N,M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]

"""
なんかどこかのノードを軸にする（root扱いする）
a -> bまでの辺を1増やす = root -> a と、root -> b までの辺を1増やす。
全ての辺のコストが偶数なら、この足す処理が偶数回されてるはず。
間にどのノードが入るかとかあるけど、奇数回足される（奇数回出てくる）なら、ダメな気がする
少なくとも木ではあるのだから、あるaからあるbに行くときに必ずとおるrootがあるはずなので、これでいいんじゃなかろうか
"""

arr = [0] * N
for a,b in ab:
    arr[a-1] += 1
    arr[b-1] += 1

ans = "YES"
for n in arr:
    if n % 2 == 1:
        ans = "NO"

print(ans)