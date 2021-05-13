from math import floor

N, K = map(int, input().split())

if K == 0:
    print(N * N)
    exit()

ans = 0
for b in range(1, N + 1):
    # [1, N]をbで割る
    num = N // b
    rem = N % b
    # numの中がK以上である個数
    # あまり: 0, 1, 2, ..., b - 1
    fact = b - 1 - K + 1
    if fact > 0:
        ans += num * fact
    
    # 残った分
    ans += max(0, rem - K + 1)
    # print(b, num, rem, num * fact, rem)
print(ans)