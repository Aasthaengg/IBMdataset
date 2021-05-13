h, w = map(int, input().split())
A = []
for i in range(h):
    s = list(map(int, input().split()))
    A.append(s)

#print(A)
S = []
for i in range(h):
    if i & 1:
        for j in range(w-1):
            if A[i][j] & 1:
                S.append([i+1, j+1, i+1, j+2])
                A[i][j+1] += 1
        if A[i][w-1] & 1 and i < h-1:
            S.append([i+1, w, i+2, w])
            A[i+1][w-1] += 1
    else:
        for j in reversed(range(1, w)):
            if A[i][j] & 1:
                S.append([i+1, j+1, i+1, j])
                A[i][j-1] += 1
        if A[i][0] & 1 and i < h-1:
            S.append([i+1, 1, i+2, 1])
            A[i+1][0] += 1

print(len(S))
for x in S:
    print(" ".join([str(n) for n in x]))
