n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b = b[::-1]

ua = [0 for i in range(n)]
fa = [False for i in range(n)]
ub = [0 for i in range(n)]
fb = [False for i in range(n)]


bm = 0
for i in range(n):
    if a[i] > bm:
        ua[i] = a[i]
        fa[i] = True
        bm = a[i]
    else:
        ua[i] = bm

bm = 0
for i in range(n):
    if b[i] > bm:
        ub[i] = b[i]
        fb[i] = True
        bm = b[i]
    else:
        ub[i] = bm
ub = ub[::-1]
fb = fb[::-1]
ans = 1
m = 10**9+7

for i in range(n):
    if fa[i] and fb[i]:
        if not ua[i] == ub[i]:
            ans = 0
            break
    elif fa[i] or fb[i]:
        if ua[i] > ub[i]:
            if not fb[i]:
                ans = 0
                break
        elif ua[i] == ub[i]:
            ans = ans
        else:
            if not fa[i]:
                ans = 0
                break
    else:
        ans *= min(ua[i],ub[i])
        ans %= m
    # print(ans)

print(ans)

# print(ua)
# print(fa)
# print(ub)
# print(fb)









