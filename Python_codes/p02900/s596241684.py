from math import*
def factrization_prime(number):
    factor = {}
    div = 2
    s = sqrt(number)
    while div < s:
        div_cnt = 0
        while number % div == 0:
            div_cnt += 1
            number //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if number > 1:
        factor[number] = 1
    return factor
A, B = map(int, input().split())
f = factrization_prime(gcd(A,B))
print(len(f)+1)
