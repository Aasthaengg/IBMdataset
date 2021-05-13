def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

N = int(input())
S = input()
MAX = 0

for i in range(N-1):
    A = z_algo(S[i:])
    for j in range(len(A)):
        if MAX < A[j] and A[j] <= j:
            MAX = A[j]

print(MAX)