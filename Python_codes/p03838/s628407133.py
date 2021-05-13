def solve(x: int, y: int) -> int:
    if abs(x) > abs(y):
        return solve(-y, -x)
    m = 0
    if x < 0:
        m += 1
    if y < 0:
        m += 1
    return abs(y) - abs(x) + m


def test():
    assert solve(1, 10) == 9
    assert solve(-1, 10) == 10
    assert solve(1, -10) == 10
    assert solve(-1, -10) == 11

    assert solve(10, 1) == 11
    assert solve(-10, 1) == 10
    assert solve(-10, -1) == 9
    assert solve(10, -1) == 10

    assert solve(10, 20) == 10
    assert solve(10, -10) == 1
    assert solve(-10, -20) == 12
    assert solve(-10, 10) == 1


if __name__ == "__main__":

    x, y = [int(x) for x in input().split(" ")]

    print(solve(x, y))