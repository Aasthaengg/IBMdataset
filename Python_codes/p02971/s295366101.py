N = int(input())
A = [int(input()) for i in range(N)]
a_sorted = sorted(A,reverse=True)
for i in range(N):
    if A[i] != a_sorted[0]:
        print(a_sorted[0])
    elif A[i] == a_sorted[0]:
        print(a_sorted[1])