import collections

n,m = map(int,input().split())

## 素因数を並べる関数。collections.counterで受ける。
def prime_factorize(K):
    ans = []
    i = 2
    while i ** 2 <= K:
        if K % i == 0:
            K = K//i
            ans.append(i)
        else:
            i += 1
    if K != 1:
        ans.append(K)

    return ans

def combination(N, r):
    ans = N
    mod = pow(10, 9) + 7
    for i in range(1, r):
        ans = ans * ((N - i) % mod) * pow(i + 1, mod - 2, mod)
        ans = ans % mod
    
    return ans
 
prime_nums = dict(collections.Counter(prime_factorize(m)))

ans = 1
mod = pow(10, 9) + 7
for num in prime_nums.values():
    ans = ans * combination(n - 1 + num, num)
    ans = ans % mod

print(ans)

