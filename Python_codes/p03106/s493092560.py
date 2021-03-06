import math

def make_divisors(n):
    #https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a,b,k = map(int,input().split())
tmp = math.gcd(a,b)
ans = make_divisors(tmp)
print(ans[-k])