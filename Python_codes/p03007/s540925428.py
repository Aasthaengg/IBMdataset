N = int(input())
a = list(map(int, input().split()))
a.sort()
t = 0
for m in range(N):
    if a[m] < 0:
        t += 1
if N > 2:
    if t == 0:
        c = a[0]
        for i in range(N - 2):
            c = c - a[N - 1 - i]
        d = a[1] - c
        print(d)
        e = a[0]
        f = a[N - 1]
        for j in range(N - 2):
            print(e, end = ' ')
            print(f)
            e = e - f
            f = a[N - 2 - j]
        print(a[1], end = ' ')
        print(e)
    elif t > 0 and t < N - 1:
        c = 0
        for i in range(t):
            c += a[i] 
        for j in range(N - t -1):
            c = c - a[t + 1 + j]
        d = a[t] - c
        print(d)
        e = a[0]
        f = a[N - 1]
        for k in range(N - t - 1):
            print(e, end = ' ')
            print(f)
            e = e - f
            f = a[N - 2 - k]
        a[0] = e
        g = a[t]
        for l in range(t):
            print(g, end = ' ')
            print(a[l])
            g = g - a[l]
    elif t == N - 1 or t == N:
        c = a[N - 1]
        for i in range(N - 1):
            c = c - a[i]
        print(c)
        d = a[N - 1]
        for j in range(N - 1):
            print(d, end = ' ')
            print(a[j])
            d -= a[j]
else:
    print(a[1] - a[0])
    print(a[1], end = ' ')
    print(a[0])