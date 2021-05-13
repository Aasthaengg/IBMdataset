N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

sum1 = sum(B)

cn = 0
SUM = 0

for i in range(N-1):
    if A[i] + 1 == A[i+1]:
        SUM = SUM + C[A[i]-1]
        




print(sum1 + SUM)