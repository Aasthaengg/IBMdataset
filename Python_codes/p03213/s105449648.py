# 解説AC
# 約数75になる条件は、素因数分解した際の約数の数p, q,..について
# (p+1)*(q+1)*..=75となること
# 先に上式を満たす(p,q, ..)組み合わせを列挙して、
# N!の素因数分解に対して、各組み合わせを満たすものを数え上げる

n = int(input())

# 素因数分解
def prime_factorization(n):
    Primes = []
    while n % 2 == 0:
        Primes.append(2)
        n = int(n/2)
    f = 3
    while f*f <= n:
        if n % f == 0:
            Primes.append(f)
            n = int(n/f)
        else:
            f += 2
    if n != 1:
        Primes.append(n)
    return Primes

Primes_count = [0 for _ in range(n+1)]

for i in range(2,n+1):
    Primes = prime_factorization(i)
    for prime in Primes:
        Primes_count[prime] += 1

# 75 = 3*5*5 = (1*75) = (3*25) = (3*5*5) = (5*15)
def count(n, Primes_count):
    return len(list(filter(lambda x:x>=n-1, Primes_count)))

ans = 0
# 1*75
ans += count(75, Primes_count)

# 3*25 3に対する-1は25以上とのかぶりを避けるため。
ans += (count(3, Primes_count)-1) * count(25, Primes_count)

# 5*15 上と同様
ans += (count(5, Primes_count)-1) * count(15, Primes_count)

# 3*5*5 5以上を一つ決める->残りから5以上を一つ決める->残りから3以上を1つ決める->5同士の入れ替えが起きるので2で割り切り捨てる
ans += (count(5, Primes_count)) * (count(5, Primes_count) -1) * (count(3, Primes_count)-2) // 2

print(ans)