N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ans = 1
if N == K:
    for a in A:
        ans *= a
        ans %= MOD
    print(ans)
    exit(0)

if N - A.count(0) < K:
    print(0)
    exit(0)

plus = []
minus = []
for a in A:
    if a > 0:
        plus.append(a)
    else:
        minus.append(a)

if K % 2 == 1 and len(plus) == 0:
    minus.sort(reverse=True)
    for i in range(K):
        ans *= minus[i]
        ans %= MOD
    print(ans)
    exit(0)

plus.sort(reverse=True)
minus.sort()

if len(minus) == 0:
    for k in range(K):
        ans *= plus[k]
        ans %= MOD
    print(ans)
    exit(0)

i = 0
j = 0

if K % 2 == 1:
    ans = plus[0]
    K -= 1
    plus = plus[1:]

for _ in range(K//2):
    if i+1 >= len(plus):
        ans *= (minus[j] * minus[j+1])
        ans %= MOD
        j += 2
        continue
    elif j+1 >= len(minus):
        ans *= (plus[i] * plus[i+1])
        ans %= MOD
        i += 2
        continue

    a = plus[i] * plus[i+1]
    b = minus[j] * minus[j+1]
    if a > b:
        ans *= a
        i += 2
    else:
        ans *= b
        j += 2
    ans %= MOD

print(ans)
