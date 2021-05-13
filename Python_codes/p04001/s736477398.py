s = input()
n = len(s) - 1
ans = 0
for bit in range(1 << n):
    now = 0
    for i in range(bit):
        if bit & (1 << i):
            ans += int(s[now : i + 1])
            now = i + 1
    ans += int(s[now : len(s)])
print(ans)
