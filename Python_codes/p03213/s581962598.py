def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def calc(p, N):
    ans = 0
    while N != 0:
        N //= p
        ans += N
    return ans

N = int(input())
P = primes(N)
count = []
for i in range(len(P)):
    count.append(calc(P[i], N))
ans = 0
for i in range(len(P)):
    if count[i] >= 74:
        ans += 1

for i in range(len(P)-1):
    for j in range(i+1, len(P)):
        if count[i] >= 2 and count[j] >= 24:
            ans += 1
        if count[i] >= 24 and count[j] >= 2:
            ans += 1
        if count[i] >= 4 and count[j] >= 14:
            ans += 1
        if count[i] >= 14 and count[j] >= 4:
            ans += 1

for i in range(len(P)-2):
    for j in range(i+1, len(P)-1):
        for k in range(j+1, len(P)):
            if count[i] >= 2 and count[j] >= 4 and count[k] >= 4:
                ans += 1
            if count[i] >= 4 and count[j] >= 2 and count[k] >= 4:
                ans += 1
            if count[i] >= 4 and count[j] >= 4 and count[k] >= 2:
                ans += 1

print(ans)