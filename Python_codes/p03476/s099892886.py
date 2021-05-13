def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

p = [0] * (10 ** 5)
for i in range(10**5):
    if i % 2 == 0:
        continue
    if is_prime(i) and is_prime((i+1)//2):
        p[i] = 1

acm = [0] * (10 ** 5 + 1)
for i in range(10**5):
    acm[i+1] = acm[i] + p[i]
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(acm[r+1] - acm[l])