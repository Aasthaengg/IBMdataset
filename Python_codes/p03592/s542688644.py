n, m, k= map(int, input().split())
for p in range(m+1):
    for q in range(n+1):
        t = n*p + m*q - 2*p*q
        if t == k:
            print('Yes')
            exit()
else:
    print('No')