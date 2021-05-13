N = int(input())
A = list(map(int, input().split()))

prod_max = 10**18
prod = A[0]

if 0 in A:
    print(0)
else:
    for i in range(N-1):
        prod *= A[i+1]
        if prod > prod_max:
            print('-1')
            break
        if i == N - 2:
            print(prod)