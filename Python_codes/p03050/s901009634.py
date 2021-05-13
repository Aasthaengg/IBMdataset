from sys import stdin
N = int(stdin.readline().rstrip())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ans = 0
for i in make_divisors(N):
    if i != 1:
      if N//(i-1) == N % (i-1):
          ans += (i-1)
print(ans)