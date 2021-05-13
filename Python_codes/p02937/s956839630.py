s = input()
t = input()

n = len(s)
m = len(t)
s += s
next = [[-1] * 26 for _ in range(len(s) + 1)]

# 場所iから、次の文字jへの場所、みたいなテーブル
# 後ろから更新してくと最短距離になる
# next[i]は場所iを含む
for i in range(len(s) - 1, -1, -1):
    c = ord(s[i]) - ord('a')
    for j in range(26):
        if j == c:
            next[i][j] = i
        else:
            next[i][j] = next[i + 1][j]
now = 0
ans = 0
for i in range(m):
    c = ord(t[i]) - ord('a')
    if next[now][c] == -1:
        print(-1)
        exit()
    ans += next[now][c] - now + 1
    now = next[now][c] + 1
    if now >= n:
        now -= n
print(ans)
