def func(cnt, cn):
    tmp = [0] * 13
    for i in range(13):
        nn = (cn + i) % 13
        tmp[nn] = cnt[i]
    return tmp


MOD = 10**9+7

s = list(input())
s.reverse()

cnt = [0]*13
cnt[0] = 1
t = 1
for ci in range(len(s)):
    t %= 13 
    if s[ci] != '?':
        cn = int(s[ci]) * t % 13
        cnt = func(cnt, cn)
    else:
        tmp = [0]*13
        add = [0]*13
        for cj in range(10):
            cn = cj * t % 13
            add = func(cnt, cn)
            for _ in range(13):
                tmp[_] += add[_]
                tmp[_] %= MOD
        cnt = tmp
    t *= 10
print(cnt[5])