n = int(input())
a = list(map(int,input().split()))

m = 1000
kabu = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        x = m//a[i]
        kabu += x
        m -= x*a[i]
    else:
        m += kabu*a[i]
        kabu = 0
print(m+(kabu*a[-1]))