n, k = map(int, input().split())
s = input()
pre = "O"
cnt = 0
for i in range(n):
    now = s[i]
    if now != pre:
        cnt += 1
    pre = now
print(min((n - cnt + 2 * k), n - 1))

