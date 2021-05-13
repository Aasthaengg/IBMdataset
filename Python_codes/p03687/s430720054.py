S = input()

ans = len(S)
for i, s in enumerate(S[::-1]):
    #print(i, s, S[:-(i+1)])
    m, n = 0, 0
    for j, c in enumerate(S[:-(i+1)][::-1]):
        if c == s:
            n = max(m, n)
            m = 0
        else:
            m += 1
    n = max(m, n)
    ans = min(ans, max(i, n))
    #print(m, n, i, ans)
print(ans)