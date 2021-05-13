def solve(x):
    # 方針: ただ 6->5 を繰り返すだけ
    return 2 * (x // 11) + (0 if x % 11 == 0 else 1 if x % 11 <= 6 else 2)

_x = int(input())
print(solve(_x))