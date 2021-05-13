q = int(input())

L = [True] * (10**5 + 1)

L[0], L[1] = False, False

for i in range(2, int((10**5) ** 0.5) + 1):
    if not L[i]:
        continue
    j = 2
    while i * j <= 10**5:
        L[i * j] = False
        j += 1

A = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    if L[i] and L[(i+1)//2]:
        A[i] = A[i-1] + 1
    else:
        A[i] = A[i-1]

for i in range(q):
    l, r = map(int, input().split())
    if l == r:
        if L[l] and L[(l+1)//2]:
            print(1)
        else:
            print(0)
    else:
        if L[l] and L[(l+1)//2]:
            print(A[r] - A[l-1])
        else:
            print(A[r] - A[l])