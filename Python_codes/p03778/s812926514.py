

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    W, a, b = read_ints()
    if a+W <= b:
        return abs(a+W-b)
    if b+W <= a:
        return abs(b+W-a)
    return 0


if __name__ == '__main__':
    print(solve())
