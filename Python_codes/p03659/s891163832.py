n = int(input())
a = list(map(int,input().split()))
s1 = sum(a) - a[0]
s2 = a[0]
m = abs(s1-s2)
for i in range(1,n-1):
    s1 -= a[i]
    s2 += a[i]
    m = min(m,abs(s1-s2))
print(m)