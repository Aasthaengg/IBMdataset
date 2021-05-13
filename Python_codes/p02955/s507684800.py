N, K = map(int, input().split())
A = [int(i) for i in input().split()]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors


lst = make_divisors(sum(A))

for l in lst:
    cnt_m, cnt_p = 0, 0
    ml = sorted([i % l for i in A])
    for m in ml:
        if cnt_m <= K-m:
            cnt_m += m
        else:
            cnt_p += l-m
    if cnt_m <= K and cnt_p <= K:
        print(l)
        exit()
print(1)
