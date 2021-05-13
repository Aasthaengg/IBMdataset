N = int(input())
A = [int(input()) for i in range(N)]
A2 = sorted(A)
for i in A:
    if i == A2[N-1]:
        print(A2[N-2])
    else:
        print(A2[N-1])
