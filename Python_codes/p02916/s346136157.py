N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

happy = sum(B)

for j in range(N-1):
    if A[j+1] - A[j] == 1:
        happy +=  C[A[j]-1]

print(happy)
