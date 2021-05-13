s = input()
n = len(s)
ans = float("Inf")
for i in range(n):
    x = s[i]
    t = list(s)
    c = 0
    for j in range(n-1):
        if t.count(x) == len(t):
            break
        for k in range(len(t)-1):
            if t[k+1] == x:
                t[k] = x
        c += 1
        t = t[:len(t)-1]
    ans = min(ans, c)
print(ans)