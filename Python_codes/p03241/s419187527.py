import math
N, M = map(int, input().split())

def factorization(n):
    factor_list = []
    if n < 1:
        return factor_list
    limit = int(math.sqrt(n))+1
    for i in range(1, limit):
        if n % i == 0:
            factor_list.append(i)
            if not n == i**2:
                factor_list.append(n//i)
    factor_list.sort()
    return factor_list

factor = factorization(M)


ans = 1
for f in factor:
    if N * f <= M and f > ans:
        ans = f
print(ans)