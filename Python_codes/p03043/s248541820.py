n, k = map(int, input().split())
p = 0

for i in range(1, n+1):
    pp = 1/n;
    x = 1
    while i * x < k:
        x *= 2 
        pp *= 0.5
    p += pp
print(p)

