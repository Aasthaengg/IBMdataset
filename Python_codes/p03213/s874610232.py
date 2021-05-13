def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    count = 0
    for i in range(2, n+1):
        if prime[i]:
            count += 1
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime


def count(p):
    cnt = 0
    n = N
    while n > 0:
        n //= p
        cnt += n
    return cnt


N = int(input())
prime = sieve(N)
ans = 0

# case 1: p^74
for p in range(N+1):
    if not prime[p]:
        continue
    if count(p) < 74:
        break
    ans += 1

# case 2: p^2 q^4 r^4
for p in range(N+1):
    if not prime[p]:
        continue
    if count(p) < 2:
        break
    for q in range(N):
        if not prime[q] or p == q:
            continue
        if count(q) < 4:
            break
        for r in range(q+1, N+1):
            if not prime[r] or p == r:
                continue
            if count(r) < 4:
                break
            ans += 1

# case 3: p^4 q^14
for p in range(N+1):
    if not prime[p]:
        continue
    if count(p) < 4:
        break
    for q in range(N+1):
        if not prime[q] or p == q:
            continue
        if count(q) < 14:
            break
        ans += 1

# case 3: p^2 q^24
for p in range(N+1):
    if not prime[p]:
        continue
    if count(p) < 2:
        break
    for q in range(N+1):
        if not prime[q] or p == q:
            continue
        if count(q) < 24:
            break
        ans += 1

print(ans)
