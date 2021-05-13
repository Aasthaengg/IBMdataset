N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divisors = make_divisors(N)

i = 0
res = 0
while True:
    l = divisors[i]
    r = divisors[-(i+1)]
    if r - 1 > l:
        res += r - 1
        i += 1
    else:
        break

print(res)