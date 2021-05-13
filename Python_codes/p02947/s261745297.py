N = int(input())
S = [None for _ in range(N)]
for i in range(N):
    s = list(input())
    s.sort()
    S[i] = ''.join(s)
S.sort()


def combination(n, k):
    num = 1
    den = 1
    for i in range(k):
        num *= n-i
        den *= i+1
    return num//den


ct = 1
ans = 0
tmp = S[0]
for i in range(1, N):
    if S[i] == tmp:
        ct += 1
    else:
        if ct >= 2:
            ans += combination(ct, 2)
        ct = 1
        tmp = S[i]
if ct >= 2:
    ans += combination(ct, 2)

print(ans)
