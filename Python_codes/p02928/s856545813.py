N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


z = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            z += 1

y = 0
for a1 in A:
    for a2 in A:
        if a1 > a2:
            y+=1

mod = 10**9 + 7

ans = z * (K) + y * (K) * (K-1)//2
print(ans % mod)

