n, p = map(int, input().split())
a = list(map(int, input().split()))
a1 = []
a2 = []
for i in range(n):
    if a[i] % 2 == 0:
        a2.append(a[i])
    else:
        a1.append(a[i])
if len(a2) == n:
    if p == 0:
        print(2**n)
    else:
        print(0)
else:
    print(2**(n-1))