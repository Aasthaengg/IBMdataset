n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

ans = 0
for i in range(len(t)):
    if i < k:
        if t[i] == "r":
            ans += p
        elif t[i] == "s":
            ans += r
        else:
            ans += s
    else:
        if t[i] == "r":
            if t[i - k] != "r":
                ans += p
            else:
                t[i] = "x"
        if t[i] == "s":
            if t[i - k] != "s":
                ans += r
            else:
                t[i] = "x"
        if t[i] == "p":
            if t[i - k] != "p":
                ans += s
            else:
                t[i] = "x"
                
print(ans)