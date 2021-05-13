import math

N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

K = int(math.log2(N-1))

if N == 2:
    print(A[0])
else:
    ans = A[0]
    ind = 1
    num = 0
    for i in range(N-2):
        if num < 2:
            ans += A[ind]
            num += 1
        else:
            ind += 1
            ans += A[ind]
            num = 1
        
    print(ans)


