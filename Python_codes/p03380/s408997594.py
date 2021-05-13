N = int(input())
A = list(map(int, input().split()))

A.sort()


ncand = A[-1]

ccand = A[0]
nhalf = ncand // 2
diff = abs(nhalf - ccand)

for i in range(1, N-1):
    d = abs(nhalf - A[i])
    if diff >= d:
        ccand = A[i]
        diff = d

print(ncand, ccand)
