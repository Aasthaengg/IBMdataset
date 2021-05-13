n = int(input())
B = [int(x) for x in input().split()]
A = [B[0]]

for i in range(n-1):
    A.append(B[i])
    if A[i] > B[i]:
        A[i] = B[i]
print(sum(A))