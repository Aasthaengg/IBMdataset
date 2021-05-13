N = int(input())
A = list(map(int, input().split()))

key = 0
for a in A:
    if abs(a) > abs(key):
        key = a
key_i = A.index(key)

m = 0
ans = []
if key > 0:
    for i in range(N):
        if A[i] < 0:
            m += 1
            A[i] += key
            ans.append([key_i+1, i+1])

    for i in range(1, N):
        if A[i-1] > A[i]:
            A[i] += A[i-1]
            m += 1
            ans.append([i, i+1])

    print(m)
    for x, y in ans:
        print(x, y)

elif key < 0:
    for i in range(N):
        if A[i] > 0:
            m += 1
            A[i] += key
            ans.append([key_i+1, i+1])

    for i in range(N-1, 0, -1):
        if A[i-1] > A[i]:
            A[i-1] += A[i]
            m += 1
            ans.append([i+1, i])

    print(m)
    for x, y in ans:
        print(x, y)

else:
    print(0)