N, K = map(int, input().split())
A = list(map(int, input().split()))

# nの約数を求める。計算量O(sqrt(N))
def get_divisors(n):
    from math import sqrt, ceil
    from collections import deque
    divisors = deque([])
    for num in range(ceil(sqrt(n)), n+1):
        if n % num == 0:
            divisors.append(n//num)
            if n//num != n:
                divisors.appendleft(num)
    return list(divisors)


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors

total = sum(A)
divisors = make_divisors(total)
ans = -1
for d in divisors:
    R = [a%d for a in A]
    R.sort(reverse=True)
    pr = 0
    nr = -sum(R)
    for i, r in enumerate(R):
        pr += d-r
        nr += r
        if nr+pr >= 0:
            if pr <= K and nr+pr == 0:
                ans = d
            break
    if ans != -1:
        print(ans)
        break
else:
    print(1)
