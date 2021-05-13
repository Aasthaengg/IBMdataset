n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(len(B)):
    cB = B[i]
    if A[i] > cB:
        ans += cB
    else:
        ans += A[i]
        cB -= A[i]
        if cB > A[i+1]:
            ans += A[i+1]
        else:
            ans += cB
        A[i+1] = max(0, A[i+1]-cB)
print (ans)