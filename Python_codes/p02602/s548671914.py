N,K = map(int, input().split())
A = list(map(int, input().split()))

a = 0
while K < N:
    if A[a] < A[K]:
        print("Yes")
    else:print("No")
    K += 1
    a += 1