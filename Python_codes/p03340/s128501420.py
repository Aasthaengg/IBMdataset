N = int(input())
A = list(map(int, input().split()))

# BT = [[0] * 20 for _ in range(N + 1)]
# for i, a in enumerate(A):
#     j = 0
#     while a > 0:
#         BT[i + 1][j] += (a & 1)
#         j += 1
#         a >>= 1
# print(BT)
# S = [[0] * 20 for _ in range(N + 1)]
# for j in range(20):
#     for i in range(N):
#         S[i + 1][j] = S[i][j] + BT[i][j]
# # print(S)

S = 0
X = 0
l = 0
cnt = 0
for r in range(N):
    S += A[r]
    X ^= A[r]
    if S == X:
        cnt += r - l + 1
    else:
        while l != r:
            S -= A[l]
            X ^= A[l]
            l += 1
            if S == X:
                cnt += r - l + 1
                break

print(cnt)
