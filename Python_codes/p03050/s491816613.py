N = int(input())

def make_divisors(n):
    import math
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: #割り切れるとき
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

ans = 0
lst = make_divisors(N)
for X in lst:
    m = N // X - 1
    if m > X:
        ans += N // X - 1

print (ans)
# print (lst)