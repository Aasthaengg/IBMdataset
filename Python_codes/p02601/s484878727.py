A, B, C = map(int, input().split())
K = int(input())

for i in range(K+1):
    if A<B*2**i<C*2**(K-i):
        print('Yes')
        break
else:
    print('No')