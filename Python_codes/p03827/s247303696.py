

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    x = 0
    max_x = 0
    n = read_int()
    for c in input().strip():
        if c == 'I':
            x += 1
        else:
            x -= 1
        max_x = max(max_x, x)
    return max_x


if __name__ == '__main__':
    print(solve())
