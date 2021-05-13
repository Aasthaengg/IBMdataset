import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
def resolve():
    N = ir()
    ans = len(make_divisors(N-1))-1
    d = make_divisors(N)
    d.remove(1)
    for i in d:
        tmp = N
        while tmp != 1 and tmp >= i:
            if tmp%i > 0:
                tmp %= i
            else:
                tmp //= i
        if tmp == 1:
            ans += 1
    print(ans)
resolve()