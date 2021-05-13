n = int(input())
ts = list(map(int, input().split()))
xs = list(map(int, input().split()))

ts = [0] + ts + [ts[-1]]
xs = [xs[0]] + xs + [0]

if n == 1:
    if xs[1] == ts[1]:
        print(1)
    else:
        print(0)
else:
    m = 10**9 + 7
    a = 1
    for i in range(1, n+1):
        if ts[i-1]==ts[i] and xs[i]==xs[i+1]:
            a = a*min(ts[i], xs[i]) % m
        else:
            if ts[i-1]<ts[i] and xs[i]>xs[i+1]:
                if ts[i]!=xs[i]:
                    a = 0
            elif ts[i-1]<ts[i]:
                if xs[i]<ts[i]:
                    a = 0
            else:
                if ts[i]<xs[i]:
                    a = 0
    print(a)