N, H, W = map(int, input().split())
A = []
B = []
for i in range(N):
    A_, B_ = map(int, input().split())
    A.append(A_)
    B.append(B_)

ans = 0
for i in range(N):
    if A[i] >= H and B[i] >= W:
        ans += 1

print(ans)