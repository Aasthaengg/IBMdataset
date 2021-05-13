s = input()
ans = 10 ** 10
for i in range(26):
    c = chr(ord("a") + i)
    s_c = list(s)
    cnt = 0
    while len(set(s_c)) != 1:
        t = ""
        for i in range(len(s_c) - 1):
            if s_c[i + 1] == c:
                t += c
            else:
                t += s_c[i]
        cnt += 1
        s_c = t
    ans = min(ans, cnt)

print(ans)