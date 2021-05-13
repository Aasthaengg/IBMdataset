MOD = 10**9 + 7
N = int(input())
*T, = map(int, input().split())
*A, = map(int, input().split())
ans = 1
for i in range(N):
    temp1 = -1
    temp2 = -1
    if i == 0 or T[i-1] < T[i]:
        temp1 = T[i]
    if i == N-1 or A[i] > A[i+1]:
        temp2 = A[i]

    if temp1 == -1 and temp2 == -1:
        ans = (ans * min(T[i], A[i])) % MOD
    elif temp1 == -1 and temp2 != -1:
        if temp2 > T[i]: ans = 0; break
    elif temp1 != -1 and temp2 == -1:
        if temp2 > A[i]: ans = 0; break
    else:
        if temp1 != temp2: ans = 0; break
print(ans)