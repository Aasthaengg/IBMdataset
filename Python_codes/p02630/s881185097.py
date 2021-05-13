ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y
nom = [0] * (10**5+1)
n = ini()
a = inl()
ans = sum(a)
for i in a:
        nom[i] += 1
q = ini()
for i in range(q):
        b,c = inm()
        d = c-b
        ans += nom[b] * d
        print(ans)
        nom[c] += nom[b]
        nom[b] = 0
