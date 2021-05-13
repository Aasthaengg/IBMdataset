N = int(input())
A = [int(i) for i in input().split()]

if min(A) >= 0:
    print(N-1)
    for i in range(1, N):
        print(i, i+1)
elif max(A) <= 0:
    print(N-1)
    for i in range(1, N):
        print(N-i+1, N-i)
else:
    if max(A) > - min(A):
        M = 0
        M_index = 0
        for i in range(N):
            if M < A[i]:
                M = A[i]
                M_index = i
        ans = []
        for i in range(N):
            if A[i] < 0:
                ans.append((M_index+1, i+1))
        print(len(ans)+N-1)
        for x, y in ans:
            print(x, y)
        for i in range(1, N):
            print(i, i + 1)

    else:
        M = 0
        M_index = 0
        for i in range(N):
            if M > A[i]:
                M = A[i]
                M_index = i
        ans = []
        for i in range(N):
            if A[i] > 0:
                ans.append((M_index+1, i+1))
        print(len(ans)+N-1)
        for x, y in ans:
            print(x, y)
        for i in range(1, N):
            print(N - i + 1, N - i)
