n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())
ans = 0

for i in range(n):
    if i < k:
        if t[i] == "r":
            ans += p
        elif t[i] == "s":
            ans += r
        else:
            ans += s
    else:
        if t[i] != t[i - k]:
            if t[i] == "r":
                ans += p
            elif t[i] == "s":
                ans += r
            else:
                ans += s
        else:
            t[i] = ""

print(ans)