N, L = map(int, input().split())
A = [0]*N
for i in range(N):
    A[i] = L + (i+1) - 1

ans = 0
if 0 in A:
    ans = sum(A)
else:
    if L < 0:
        ans = sum(A) - A[-1]
    else:
        ans = sum(A) - A[0]

print(ans)