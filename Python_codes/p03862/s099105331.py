n,x = map(int, input().split())
A =list(map(int, input().split()))

ans = 0
for i in range(n-1):
    y =  A[i]+A[i+1]
    if y > x:
        r = y-x
        if A[i+1] >= r:
            A[i+1] -= r
            ans += r
        else:
            A[i+1] = 0
            A[i] -= (r-A[i+1])
            ans += r
print(ans)
