N = int(input())
A = [int(i) for i in input().split()]

S = min(A)
L = max(A)

c = 0
B = []

if S == L:
    pass

elif S >= 0 and L > 0:
    for i in range(N-1):
        if A[i+1] >= A[i]:
            pass
        else:
            A[i+1] += A[i]
            c += 1
            B.append((i+1, i+2))

elif L <= 0 and S < 0:
    for i in range(N-1):
        if A[-i-2] <= A[-i-1]:
            pass
        else:
            A[-i-2] += A[-i-1]
            c += 1
            B.append((N-i, N-i-1))

else:
    if L >= -S:
        l = A.index(L)
        if A[0] < 0:
            A[0] += L
            c += 1
            B.append((l+1, 1))
        for i in range(N-1):
            if A[i+1] >= A[i]:
                pass
            else:
                if A[i+1] < 0:
                    A[i+1] += L
                    c += 1
                    B.append((l+1, i+2))
                A[i+1] += A[i]
                c += 1
                B.append((i+1, i+2))
                if i+1 == l:
                    L = A[l]
    else:
        s = A.index(S)
        if A[-1] > 0:
            A[-1] += S
            c += 1
            B.append((s+1, N))
        for i in range(N-1):
            if A[-i-2] <= A[-i-1]:
                pass
            else:
                if A[-i-2] > 0:
                    A[-i-2] += S
                    c += 1
                    B.append((s+1, N-i-1))
                A[-i-2] += A[-i-1]
                c += 1
                B.append((N-i, N-i-1))
                if -i-2 == s:
                    S = A[s]

if c == 0:
    print(c)
else:
    print(c)
    for i in range(c):
        print(B[i][0], B[i][1])
