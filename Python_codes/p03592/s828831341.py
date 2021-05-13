n,m,k = map(int, input().split())

for i in range(n+1):
    for j in range(m+1):
        check = i*(m-j) + j*(n-i)
        if check == k:
            print('Yes')
            exit()
else:
    print('No')