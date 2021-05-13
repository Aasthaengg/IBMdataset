s = input().split()
N = int(s[0])
K = int(s[1])
A = input().split()

for i in range(K, N):
    m1 = int(A[i - K])
    m2 = int(A[i])
    print('Yes' if m1 < m2 else 'No')
