n,k = map(int,input().split())
p = 0
for i in range(1,n+1):
    m = i
    x = 0
    while m < k:
        m *= 2
        x += 1
    p += ((1 / 2) ** x) * (1 / n)
print(p)