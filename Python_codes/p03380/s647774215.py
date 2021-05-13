n = int(input())
a = list(map(int,input().split()))

a.sort()
m = a[-1]
br = m/2
tmp = m
for i in range(n):
    if tmp > abs(a[i]-br):
        r = a[i]
        tmp = abs(a[i]-br)

print(m,r)

