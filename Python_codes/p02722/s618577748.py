n = int(input())
ans = 0
def factorize(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.append(n)
    return divisors

def check(num, mod):
    if num % mod == 1:
        return 1
    elif num % mod == 0:
        num = num / mod
        return check(num, mod)
    else:
        return 0


nfct = factorize(n)
n_1fct = factorize(n - 1)
if n_1fct != [1]:
  ans += len(n_1fct)
for mod in nfct:
  ans += check(n,mod)
print(ans)
