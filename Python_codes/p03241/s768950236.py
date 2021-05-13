n, m = map(int,input().split())

if m//n == m/n:
    print(m//n)
else:
    ans = 1
    for i in range(2,min(m,10**8+1)):
        if m-i*(n-1) < i:
            break
        if m%i == 0:#from (M-i*(N-1))%i==0
            ans = i
    print(ans)