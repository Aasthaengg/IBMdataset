N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

e = 0
for i in range(N):
    e = e+B[A[i]-1]
    if i < N-1:
        if A[i]+1==A[i+1]:
            e = e+C[A[i]-1]

print(e)
