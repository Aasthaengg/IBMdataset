import sys
sys.setrecursionlimit(10 ** 9)

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

T1, T2 = rl()
A1, A2 = rl()
B1, B2 = rl()

if T1 * A1 + T2 * A2 == T1 * B1 + T2 * B2:
    print('infinity')
    exit()
if (A1 > B1 and A1 * T1 + A2 * T2 > B1 * T1 + B2 * T2) or \
        (A1 < B1 and A1 * T1 + A2 * T2 < B1 * T1 + B2 * T2):
    print(0)
    exit()
diff = abs(A1-B1) * T1
diff2 = abs(T1 * A1 + T2 * A2 - (T1 * B1 + T2 * B2))
x, y = divmod(diff, diff2)
print(x * 2 if y == 0 else x * 2 + 1)
