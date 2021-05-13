def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
cnt = [0]*1001
div = []
for i in range(2, n+1):
    div += prime_factorize(i)

for x in div:
    cnt[x] += 1

m = 1
for i in range(len(cnt)):
    if cnt[i] > 0:
        m *= (cnt[i]+1)
print(m % (10**9+7))