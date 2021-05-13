def comb(n,k,p):
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) %p
    b=factorial(k) %p
    c=factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p

n, k = map(int, input().split())
mod = 10**9 + 7
red_num = n - k
blue_num = k
ans = []
for i in range(1, k+1):
    must_red = i - 1
    rest_red = red_num - must_red
    red_space = i + 1
    must_blue = i
    rest_blue = blue_num - must_blue
    blue_space = i
    if rest_red < 0 or rest_blue < 0:
        ans.append(0)
        continue

    red_pattern = comb(rest_red + red_space - 1, red_space - 1, mod)
    blue_pattern = comb(rest_blue + blue_space - 1, blue_space - 1, mod)
    ans.append((red_pattern * blue_pattern) % mod)

for i in range(k):
    print(ans[i])