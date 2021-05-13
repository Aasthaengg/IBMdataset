from bisect import bisect_left
from itertools import accumulate
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

# にぶたん: Ai + Aj が X以上となるようなものがM通り以上あるか？
ok, ng = 0, 2 * 10 ** 5 + 1
while abs(ok - ng) > 1:
    X = (ok + ng) // 2
    cnt = 0
    for a in A:
        cnt += N - bisect_left(A, X - a)
        if cnt >= M:
            ok = X
            break
    else:
        ng = X

# 規定値以上のものを全てとる（ギリギリK個を超える）
ans = 0
cnt = 0
A_acc = [0] + list(accumulate(A[::-1]))[::-1]

for a in A:
    i = N - bisect_left(A, ok - a)
    cnt += i
    ans += a * i + A_acc[-i]

# 取りすぎた分を削る
ans -= max(0, cnt - M) * ok
print(ans)
