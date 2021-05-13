s = input()

# https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2019/0817_agc037

ans = 0
prev = ''
i = 0
while i < len(s):
    c = s[i]
    # 前の文字と現在の文字が同じ
    if c == prev:
        i += 1
        if i == len(s):
            break
        # 2文字になる
        c += s[i]
    prev = c
    i += 1  # 次の文字へ進む
    ans += 1

print(ans)
