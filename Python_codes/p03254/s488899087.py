N, x = map(int,input().split())
a = sorted(map(int,input().split()))

A = sum(a)
if x > A:
    print(N-1)
elif x == A:
    print(N)
else:
    t = 0
    for n in range(N):
        t += a[n]
        if t > x:
            print(n)
            break