N, x = map(int, input().split())
A = [int(i) for i in input().split()]

ans = 0
for i in range(1, N):
    if A[i-1]+A[i] > x:
        e = A[i-1]+A[i]-x
        ans += e
        if A[i] >= e:
            A[i] -= e
        else:
            A[i] = 0
print(ans)
