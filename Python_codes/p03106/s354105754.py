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

def main():
    a,b,k = map(int,input().split())
    from math import gcd
    y = make_divisors(gcd(a,b))
    print(y[-k])

if __name__ == '__main__':
    main()
