s = input()
# 97=122
ans = 100
for i in range(97, 123):
    c = chr(i)
    # シュミレーションする
    t = s
    while True:
        if t.count(c) == len(t):
            ans = min(ans, len(s) - len(t))
            break
        new = ""
        for j in range(len(t) - 1):
            if t[j] == c or t[j + 1] == c:
                new += c
            else:
                new += t[j]
        t = new
print(ans)
