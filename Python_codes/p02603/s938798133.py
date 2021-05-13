n = int(input())
a = list(map(int, input().split()))

m = 1000
s = 0

for i in range(n-1):
    if a[i] < a[i+1]:
        s = m // a[i]
        m += (a[i+1]-a[i]) * s

print(m)

#溶けてないよ
