

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    6 5 6 5
    """
    x = read_int()
    answer = (x//11)*2
    if x%11 > 6:
        answer += 2
    elif x%11 > 0:
        answer += 1
    return answer


if __name__ == '__main__':
    print(solve())
