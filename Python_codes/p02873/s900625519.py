S = input()
N = len(S) + 1
A = [0]*N

cnt = 0
for i in range(N):
    A[i] = cnt
    if i == N-1:
        break
    if S[i] == "<":
        cnt += 1
    else:
        cnt = 0

cnt = 0
for i in range(N)[::-1]:
    A[i] = max(A[i], cnt)
    if i == 0:
        break
    if S[i-1] == ">":
        cnt += 1
    else:
        cnt = 0

print(sum(A))