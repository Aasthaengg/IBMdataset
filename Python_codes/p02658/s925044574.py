ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y

n = ini()
a = inl()
ans = 1
lim = 10 ** 18
for i in a:
        ans *= i
        if ans > lim:
                ans = -1
                break
if min(a) == 0:
        ans = 0
print(ans)
