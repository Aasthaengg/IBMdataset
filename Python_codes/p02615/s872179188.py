N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

if N%2 == 0:
    print(sum(A[:int(N/2)])*2 - A[0])
else:
    print(sum(A[:N//2+1])*2 - A[0] - A[N//2])

