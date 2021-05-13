N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
if A[0] != 0:
    print(-1)
    exit()

for i in range(1, N):
    if A[i] - A[i-1] > 1:  # 前の数に+1することでしか数を生成することができないため、2以上離れている場合は無理
        print(-1)
        exit()

now = A[0]
for i in range(1, N):
    if A[i] == now+1:
        ans += 1
        now = A[i]
    else:
        ans += A[i]
        now = A[i]
print(ans)
