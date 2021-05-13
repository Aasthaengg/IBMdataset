N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = sum(A)
for i, b in enumerate(B):
    if A[i] <= b:
        A[i+1] = max(0, A[i+1] - (b-A[i]))
        A[i] = 0
    else:
        A[i] = A[i] - b
print(s-sum(A))
