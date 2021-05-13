n = int(input())

cnt_a = 0   # Bで始まらないがAで終わる
cnt_b = 0   # Bで始まるがAで終わらない
cnt_ba = 0  # Bで始まりAで終わる

ans = 0
for _ in range(n):
    s = input()
    ans += s.count('AB')
    if s.endswith('A') and s.startswith('B'):
        cnt_ba += 1
    else:
        if s.endswith('A'):
            cnt_a += 1
        if s.startswith('B'):
            cnt_b += 1

if cnt_ba == 0:
    ans += min(cnt_a, cnt_b)
else:
    ans += cnt_ba-1
    if cnt_a > 0:
        cnt_a -= 1
        ans += 1
    if cnt_b > 0:
        cnt_b -= 1
        ans += 1
    # 残ったxxAとBxxを組み合わせてABを作る
    ans += min(cnt_a, cnt_b)

print(ans)