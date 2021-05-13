n = int(input())
s = input()

# 左側の黒の個数, 右側の白の個数
b, w = 0, s.count('.')
ans = min(s.count('#'), w)
for i in range(n):
    if s[i] == '#':
        b += 1
    elif s[i] == '.':
        w -= 1
    ans = min(ans, b+w)
print(ans)