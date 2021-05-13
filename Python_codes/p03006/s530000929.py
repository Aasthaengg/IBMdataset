N = int(input())
S = list(tuple(map(int, input().split())) for _ in range(N))
A = []
if N == 1:
    print(1)
else:
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            a, b = S[i]
            c, d = S[j]
            for k in range(len(A)):
                e, f, g = A[k]
                if e == a-c and f == b-d:
                    A[k] = (e, f, g+1)
                    break
            else:
                A.append((a-c, b-d, 1))
    print(N-max(list(x[2] for x in A)))


