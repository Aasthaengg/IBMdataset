n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

ans = 0
m = [0 for _ in range(n)]

for i in range(k):
    if t[i] == 'r':
        ans += p
    elif t[i] == 's':
        ans += r
    else:
        ans += s

for i in range(k, n):
    if t[i] != t[i-k] or m[i-k] == 1:
        if t[i] == "r":
            ans += p
        elif t[i] == "s":
            ans += r
        else:
            ans += s
    else:
        m[i] = 1

print(ans)
