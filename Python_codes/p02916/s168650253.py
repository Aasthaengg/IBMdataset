N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = sum(B)

for x in range(len(A)):
    if x != len(A) - 1:
        if A[x] + 1 == A[x + 1]:
            count += C[A[x]-1]
print(count)
