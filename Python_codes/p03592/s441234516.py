n,m,k = map(int,input().split())

for i in range(n):

    if (n-2*i) != 0 and (k-m*i) % (n-2*i) == 0:
        j = (k - m * i) // (n - 2 * i)
        if 0 <= j <= m:
            print('Yes')
            exit()
print('No')
