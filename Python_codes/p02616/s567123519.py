n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 1

if k == n:
    for i in range(n):
        ans *= a[i]
        ans %= mod
    print(ans)
    exit()
if max(a) < 0 and k%2 == 1:
    a.sort(reverse=True)
    for i in range(k):
        ans *= a[i]
        ans %= mod
    print(ans)
    exit()

plus, minus = [], []
for i in range(n):
    if a[i] >= 0: plus.append(a[i])
    else: minus.append(a[i])

plus.sort()
minus.sort(reverse=True)
while k > 0:
    if len(plus) >= 2 and len(minus) >= 2:
        nump = plus[-1] * plus[-2]
        numm = minus[-1] * minus[-2]
        if nump > numm or k == 1:
            ans *= plus.pop()
            ans %= mod
            k -= 1
        else:
            ans *= minus.pop()
            ans *= minus.pop()
            ans %= mod
            k -= 2
    elif len(minus) < 2:
        ans *= plus.pop()
        ans %= mod
        k -= 1
    elif len(plus) < 2:
        if k%2 == 0:
            ans *= minus.pop()
            ans *= minus.pop()
            ans %= mod
            k -= 2
        else:
            ans *= plus.pop()
            ans %= mod
            k -= 1
print(ans)