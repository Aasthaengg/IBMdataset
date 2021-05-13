import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

div = make_divisors(n)
ans = 0
for i in div:
    res = n//i-1
    if res <= 0:continue
    if n%res==i:
        ans += res

print(ans)