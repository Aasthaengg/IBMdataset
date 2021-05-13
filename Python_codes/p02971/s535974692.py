N = int(input().rstrip())
A = []
mx1 = 0
mx2 = 0
for i in range(N):
    A.append(int(input().rstrip()))
    if A[i] > mx1:
        mx1, mx2 = A[i], mx1
    elif A[i] > mx2:
        mx2 = A[i]
for j in range(N):
    if A[j] == mx1:
        print(mx2)
    else:
        print(mx1)