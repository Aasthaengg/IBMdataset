N = int(input())
B = list(map(int, input().split()))
A = [B[0],B[0]]

for i in range(N-2):
    if B[i] <= B[i+1]:
        A.append(B[i+1])
    else:
        A[i+1] = B[i+1]
        A.append(B[i+1])

print(sum(A))