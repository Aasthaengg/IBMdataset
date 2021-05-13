N = int(input())
A, B, C = [list(map(int, input().split())) for i in range(3)]

S = 0

for i in range(N):
    S += B[i]
    try:
        if A[i+1] == A[i]+1:
            S += C[A[i]-1]
    except IndexError as e:
        continue

print(S)