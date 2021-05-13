from math import factorial
n, a, b = map(int, input().split())
V = sorted(map(int, input().split()), reverse=True)

av = sum(V[:a]) / a
print(av)

def comb(m, k):
    ans = 1
    if k == 0:
        return 1
    else:
        for i in range(k):
            ans *= m - i
            ans //= i + 1
        return ans

num = V[a]
m = V.count(num)
k = V[:a].count(num)
#print(m, k, a)
if a != k:
    ans = factorial(m) // (factorial(k) * factorial(m - k))
else:
    #mCi(i:　a=>b)
    ans = 0
    for k in range(a, b+1):
        ans += comb(m, k)
print(ans)
