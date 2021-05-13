cnt = [0, 0, 0, 0]

for _ in range(3):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1


def solve():
    odd = 0
    for c in cnt:
        if c == 0:
            return False
        elif c == 1:
            odd += 1

    return odd == 2


print('YES' if solve() else 'NO')
