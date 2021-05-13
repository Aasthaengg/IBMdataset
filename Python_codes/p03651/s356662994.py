
N, K = map(int, input().split())
#print(K)

A = list(set((map(int, input().split()))))

if len(A) == 1:
    if K == A[0]:
        ans = 'POSSIBLE'
    else:
        ans = 'IMPOSSIBLE'
elif K in A:
    ans = 'POSSIBLE'
elif K > max(A):
    ans = 'IMPOSSIBLE'
else:
    A.sort()

    #print(A)

    a = A[0]
    lenA = len(A)
    for i in range(1,lenA):
        if A[i]%a > 0:
            b = A[i]
            break
        if i == lenA-1:
            b = A[1]

    while True:
        c = b - a
        if c == 0:
            break
        if c < a:
            b = a
            a = c
        else:
            b = c

    if K%a == 0:
        ans = 'POSSIBLE'
    else:
        ans = 'IMPOSSIBLE'
    #print(a)

print(ans)
