ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y

n = ini()
a = inl()
a = sorted(a,reverse = True)
c = 1
j = 0
ans = 0
for i in range(1,n):
        ans += a[j]
        c += 1
        if c == 2:
                c = 0
                j += 1
print(ans)
