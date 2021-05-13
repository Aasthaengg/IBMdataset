n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

score = B[A[0]-1]

for i in range(1,n):
    score += B[A[i]-1]
    if A[i] == A[i-1]+1:
        score += C[A[i-1]-1]
    else:
        continue
print(score)