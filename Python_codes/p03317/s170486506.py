n, k = (int(x) for x in input().split())

a = [int(x) for x in input().split()]

if n == k:
    print(1)
elif k == 2:
    print(n-1)
else:
    rem = n % (k-1)
    m = (n - rem) / (k-1)
    if rem <= 1:
        print(int(m))
    else:
        print(int(m+1))

