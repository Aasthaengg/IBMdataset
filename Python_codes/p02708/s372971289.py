# 10^100のクソデカ数値がクソデカすぎるため、+0,+1..+Nが束になってもいたくも痒くもない
# なのでもはや無視していい
# 最初の例でいうと、2つ選ぶのは[0,1,2,3]からなので、和のバリエーションは最小値1~最大値5の5つ
# 3つ選ぶのは最小値3~最大値6の4つ
# 4つ選ぶのは1つ
# 毎回最大値と最小値を計算して差+1を加えてやるとできあがり
# 計算には数列の和を使う

n, k = map(int, input().split())
mod = 10**9 + 7

ans = 1
for i in range(k, n + 1):
    # 初項0,公差1,末項i-1までの和
    min_s = i * (i - 1) // 2
    # 初項n+1-i, 公差1, 末項i-1までの和
    max_s = i * (2 * (n + 1 - i) + (i - 1)) // 2
    ans += max_s - min_s + 1
    ans %= mod
print(ans)
