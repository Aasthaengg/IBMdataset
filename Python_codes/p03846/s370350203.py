n, *A = map(int, open(0).read().split())
if n % 2:
    d = {i:2 for i in range(0, n, 2)}
    d[0] -= 1
else:
    d = {i:2 for i in range(1, n, 2)}
for a in A:
    if a in d:
        d[a] -= 1
    else:
        print(0)
        exit()

if any(d.values()):
    print(0)
else:
    print(pow(2, n//2, 10**9 + 7))