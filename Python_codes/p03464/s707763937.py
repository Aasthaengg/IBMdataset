K = int(input())
A = list(map(int,input().split()))
A.reverse()

for i in range(K):
    if i == 0:
        if A[i] != 2:
            print(-1)
            exit()
        else:
            m,M = 2,3
    else:
        m0 = m//A[i]
        M0 = M//A[i]
        if m0*A[i] >= m:
            m = m0*A[i]
        else:
            m = (m0+1)*A[i]
        M = (M0+1)*A[i]-1
        if m > M:
            print(-1)
            exit()

print(m,M)