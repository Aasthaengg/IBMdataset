n = int(input())
a = [10 ** 1,10 ** 2,10 ** 3,10 ** 4,10 ** 5]
if n in a:
    print(10)
    exit(0)

l = 10 ** 5
for i in range(1,n):
    m = n
    p = i
    q = m - 1
    z = 0
    while p > 0:
        z += p % 10
        p = p // 10
    while q > 0:
        z += q % 10
        q = q // 10
    l = min(l,z)

print(l)