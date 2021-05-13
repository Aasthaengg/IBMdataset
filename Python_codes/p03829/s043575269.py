ma = lambda :map(int,input().split())
n,a,b = ma()
X = list(ma())
xp = X[0]
ans = 0
for x in X:
    ans +=min(a*(x-xp),b)
    xp = x
print(ans)
