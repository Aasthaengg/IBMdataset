def eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    return is_prime


q = int(input())

p = eratosthenes(10 ** 5)
l = [0] * 10 ** 5
for i in range(3, 10 ** 5, 2):
    if p[i] and p[(i+1)//2]:
        l[i] = 1

sum_l = [0]
for v in l[1:]:
    sum_l.append(sum_l[-1] + v)

res = []
for _ in range(q):
    l, r = map(int, input().split())
    res.append(sum_l[r] - sum_l[l-1])

for v in res:
    print(v)