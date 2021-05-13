from collections import deque
from bisect import bisect_right
from math import ceil

N, D, A = map(int, input().split())
monsters = []
for _ in range(N):
    x, h = map(int, input().split())
    monsters.append((x, h))
monsters.sort()
#print("monsters = {}".format(monsters))
"""
どうせ左端のモンスターはいつか倒さないといけない（かつ爆弾投下順は不問）ので、
左端のモンスターから順に、なるべく爆弾を右に寄せて落としていけば良い。

BITを使って区間に爆弾のダメージを追加して考えても良いが、
ここではimos法チックな回答を与える。

仮に全ての爆弾が前モンスターに攻撃を与えるとしよう。
すると各モンスターにどれだけ流れダメージが飛んできたかは累積和で求まる。->totalで累積ダメージを管理。
しかし今回は爆弾に有効範囲があるため、有効期限切れの爆弾ダメージはtotalから除く必要がある。
そこでキューに（爆弾のダメージが入る限界線、爆弾のダメージ）を追加していき、各モンスターを見たとき
爆弾の期限が切れていたらpopleftで期限切れ爆弾を捨てていく。
（それ以降のモンスターに対してもその爆弾は期限切れなので、永久に捨て去って問題ない）。

以下のサイトの解説が参考になりました↓
https://at274.hatenablog.com/entry/2020/02/01/060000
"""

total = 0
ans = 0
q = deque([])

for i in range(N):
    x, h = monsters[i]

    # 期限切れ爆弾を捨てていき、残ったまだ有効な爆弾分の累積ダメージをモンスターに与える
    while q and q[0][0] < x:
        total -= q[0][1]
        q.popleft()
    h -= total

    # まだモンスターも体力が残っていれば、爆弾で追加ダメージを与える
    if h > 0:
        # まずはモンスターをやっつける
        times = ceil(h / A)
        ans += times
        #print("ans+={} for monster {}".format(times, i))

        # その後後ろへの流れダメージをtotalに追加し、爆弾の有効範囲をキューに追加
        damage = times * A
        total += damage
        q.append((x + 2 * D, damage))

print(ans)
