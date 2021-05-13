import sys

N = int(input())
A = list(map(int,input().split()))
A_sum = 1

if min(A) == 0:
    print(0)
    sys.exit()

else:
    for i in range(N):
        A_sum = A_sum * A[i]
        
        if A_sum > 1e18:
            print(-1)
            sys.exit()


print(A_sum)