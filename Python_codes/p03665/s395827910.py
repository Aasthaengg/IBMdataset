def comb(n,k):
    res = 1
    for i in range(1,k+1):
        res *= (n+1-i)
        res //= i
    return res


n,p = map(int, input().split())
a = list(map(int, input().split()))
a = [ai % 2 for ai in a]
odd, even = a.count(1), a.count(0)

ans = 0
for i in range(p,odd+1,2):
    ans += comb(odd, i) * pow(2, even)
print(ans)