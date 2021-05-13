MOD = 10**9 + 7
s = input()
now = [0] * 13
now[0] = 1
k = 1
for c in reversed(s):
    nxt = [0] * 13
    if c == '?':
        for i in range(10):
            a = k * i % 13
            for j in range(13):
                nxt[(j + a) % 13] += now[j]
                nxt[(j + a) % 13] %= MOD
    else:
        i = int(c)
        a = k * i % 13
        for j in range(13):
            nxt[(j + a) % 13] += now[j]
            nxt[(j + a) % 13] %= MOD
    now = nxt
    k = k * 10 % 13
print(now[5])
