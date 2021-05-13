def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    # divisors.sort()
    return divisors

a,b = map(int, input().split())
l = make_divisors(b)
l.sort(reverse=False)
res = 1
#print(l)
for x in l:
    if x <= b//a:
        res = max(x, res)
print(res)
