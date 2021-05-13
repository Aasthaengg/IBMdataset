def solve(N):
    for h in range(1, 3501):
        for n in range(1, 3501):
            v1 = 4*h*n-N*(h+n)
            v2 = N*h*n
            if v1>0 and v2>0 and v2%v1==0:
                return h, n, v2//v1

N = int(input())
h, n, w = solve(N)
print(h, n, w)
