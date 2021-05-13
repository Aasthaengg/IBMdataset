N, x = map(int, input().split())
A = list(map(int, input().split()))
K = []
for i in range(N-1):
    K.append(A[i]+A[i+1])
ans = 0
for i in range(N-1):
    if K[i] > x:
        if K[i] - A[i+1] <= x:
            ans += K[i] - x
            if i != N-2:
                K[i+1] -= K[i] - x
        else:
            ans += K[i] - x
            if i != N-2:
                K[i+1] -= A[i+1]
print(ans)