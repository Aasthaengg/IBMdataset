n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cur = 10**9
i = 0

while(i+k <= n):
    if(A[i+k-1] <= 0):
        tmp = -A[i]
    elif(A[i] <= 0):
        B = [-A[i], A[i+k-1]]
        B.sort()
        tmp = B[1] + 2 * B[0]
    else:
        tmp = A[i+k-1]
    cur = min(cur, tmp)
    i = i + 1

print(cur)
