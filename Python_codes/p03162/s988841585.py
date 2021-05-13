# Vacation
N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]
dp_a, dp_b, dp_c = [0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(N)]
dp_a[0], dp_b[0], dp_c[0] = abc[0][0], abc[0][1], abc[0][2]
for i in range(1, N):
    a, b, c = abc[i]
    dp_a[i] = max(dp_b[i-1] + a, dp_c[i-1] + a)
    dp_b[i] = max(dp_a[i-1] + b, dp_c[i-1] + b)
    dp_c[i] = max(dp_a[i-1] + c, dp_b[i-1] + c)
print(max(dp_a[-1], dp_b[-1], dp_c[-1]))