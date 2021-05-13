def get_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return divisors

n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
divisor = list(get_divisors(s))
divisor.sort(reverse=True)
for d in divisor:
    r = list(map(lambda x : x % d, a))
    r.sort()
    left = r[:]
    right = [0] * n
    right[-1] = r[-1] - d
    for i in range(1, n):
        left[i] += left[i - 1]
        right[n-i-1] = right[n-i] + r[n-i-1] - d
    for i in range(n-1):
        if left[i] == -right[i+1] and left[i] <= k:
            print(d)
            quit()
print(1)

