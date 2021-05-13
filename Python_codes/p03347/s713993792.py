N = int(input())
A = [int(input()) for _ in range(N)]
if A[0]:
    print(-1)
    exit()
ans = 0
dp = A[-1]
for a, b in zip(A[-2::-1], A[-1::-1]):
    if a == b - 1:
        continue
    elif a >= b:
        ans += dp
        dp = a
    else:
        print(-1)
        exit()
print(ans + dp)
