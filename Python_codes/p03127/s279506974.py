N = int(input())
A = list(map(int, input().split()))

while True:
    A_org = A[0:]
    min_A = max(A)
    min_index = A.index(min_A)
    for i in range(N):
        if A[i] < min_A and A[i] >= 1:
            min_A = A[i]
            min_index = i
    for i in range(N):
        if i == min_index:
            pass
        else:
            A[i] %= min_A
    if A == A_org:
        break

print(max(A))