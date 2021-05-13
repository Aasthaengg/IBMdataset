n,l = map(int,input().split())
m = 10**5
for i in range(n):
    if abs(m) > abs(i+l):
        m = abs(i+l)
        ans = i
s = l*n+n*(n-1)/2
print(int(s-(ans+l)))