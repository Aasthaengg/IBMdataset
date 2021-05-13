N = int(input())
A = [int(input()) for i in range(N)]
a, b = sorted(A, reverse = True)[0: 2]
for i in range(N):
    if A[i] == a:
        print(b)
    else:
        print(a)