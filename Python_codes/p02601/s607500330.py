A,B,C = list(map(int,input().split()))
K = int(input())
for i in range(K):
    for j in range(K-i):
        k = K-i-j
        if 2**i*A<2**j*B<2**k*C:
            print('Yes')
            exit()
print('No')