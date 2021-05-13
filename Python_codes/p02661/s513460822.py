N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

# Nが奇数の場合
if N % 2 == 1:
    min_med = A[(N - 1) // 2]
    max_med = B[(N - 1) // 2]
    ans = max_med - min_med + 1

# Nが偶数の場合
if N % 2 == 0:
    # 小数は考えにくいので、2倍した値（整数）で考える
    min_med = A[N // 2 - 1] + A[N // 2]
    max_med = B[N // 2 - 1] + B[N // 2]
    ans = max_med - min_med + 1

print(ans)
