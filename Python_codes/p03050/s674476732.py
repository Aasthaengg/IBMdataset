n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
#print(make_divisors(n))
li = make_divisors(n)
ans = 0
for l in li:
    if l == 1:
        continue
    t = l - 1
    if n % t == n//t:
        ans += t
print(ans)