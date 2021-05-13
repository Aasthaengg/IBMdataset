import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
ans = 0

#約数の列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

g = make_divisors(m)

for i in g:
    if m // i >= n:
        ans = i
print(ans)
