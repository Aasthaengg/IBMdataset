# https://atcoder.jp/contests/abc084/tasks/abc084_d

Nmax = 10**5 + 1

def prime_test(n):
    if n == 1:
        return False
    i = 2
    while i*i<=n:
        if n%i:
            i += 1
        else:
            return False
    return True

cum = [0]*Nmax

for n in range(1,Nmax,2):
    cum[n] = cum[n-2] + (prime_test(n) and prime_test((n + 1)/2))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(cum[r] - cum[l-2])
