N = int(input())
A = [0] * N
B = [0] * N

for _ in range(N):
    A[_], B[_] = map(int, input().split())

cnt = 0
for i in reversed(range(N)):
    m = (A[i] + cnt)%B[i]
    if m == 0:
        pass
    else:
        cnt += B[i] - m

print(cnt)
