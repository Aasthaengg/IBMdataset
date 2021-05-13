n = int(input())
s = input()

cnt = [0] * (n + 1)

for i in range(1, n + 1):
    cnt[i] = cnt[i - 1]
    if s[i - 1] == ".":
        cnt[i] += 1

ans = float("inf")

for i in range(0, n + 1):
    tmp = cnt[n] - cnt[i]  # cnt .. in right side
    tmp += i - cnt[i]  # cnt ## in left side
    ans = min(ans, tmp)

print(ans)
