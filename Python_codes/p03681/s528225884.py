N, M = map(int, input().split())
ans = 0

def cal(x):
    cnt = 1
    for i in range(1, x + 1):
        cnt *= i
        cnt %= (10**9 + 7)
    return cnt


if abs(N - M) >= 2:
    ans = 0
elif abs(N - M ) == 1:
    ans = (cal(N) * cal(M))  % (10**9 + 7)
else:
    ans = (cal(N) * cal(M) * 2) % (10 ** 9 + 7)

print(ans)