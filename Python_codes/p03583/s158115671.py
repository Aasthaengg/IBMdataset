import fractions
N = int(input())
for h in range(1,3501):
    for n in range(1, 3501):
        q = 4*n*h-N*(n+h)
        p = n*h*N
        if q <= 0:
            continue
        if p%q==0:
            ans = [h,n,p//q]
print(*ans)