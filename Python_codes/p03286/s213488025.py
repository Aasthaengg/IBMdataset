N = int(input())

if N == 0:
    print(0)
else:
    s = ""
    while abs(N) > 0:
        m = N % (-2)
        if m != 0:
            s = "1" + s
        else:
            s = "0" + s
        N = (N+m) // (-2)
    print(s)
