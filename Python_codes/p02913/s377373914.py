n = int(input())
s = input()

def z_algorithm(S):
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


length = n

ans = 0
for i in range(length):
    temp = z_algorithm(s[i:])
    for j in range(len(temp)):
        if min(temp[j],j) > ans:
            ans = min(temp[j],j)
print(ans)