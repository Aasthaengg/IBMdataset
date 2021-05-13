

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def count_attack(H):
    if H == 1:
        return 1
    return 2*count_attack(H//2)+1


def solve():
    H = read_int()
    return count_attack(H)


if __name__ == '__main__':
    print(solve())
