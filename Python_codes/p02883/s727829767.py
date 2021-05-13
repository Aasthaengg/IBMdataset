import math

N,K,*AF = map(int, open(0).read().split())
A = sorted(AF[:N])
F = sorted(AF[N:],reverse=True)
left = 0
right = max(A) * max(F)
while left != right:
    mid = (left+right) // 2
    temp = 0
    for i in range(N):
        temp += max(A[i]-math.floor(mid/F[i]),0)
        if temp > K:
            left = mid + 1
            break
    else:
        right = mid
print(left)