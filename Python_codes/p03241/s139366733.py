N,M=map(int,input().split())
#最大公約数のバリエーションは高々M種類？
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#約数は奇数個or偶数個
for i in reversed(make_divisors(M)):
    if M//i<N:
        pass
    else:
        print(i)
        exit()

