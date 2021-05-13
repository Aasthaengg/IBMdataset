n = int(input())
a = list(int(input()) for _ in range(n))
aa = sorted(a.copy())
mx, sd = aa[n - 1], aa[n - 2]
for i in a:
    print(mx if i < mx else sd)