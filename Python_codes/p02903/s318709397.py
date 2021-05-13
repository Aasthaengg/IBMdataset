

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def cell(i, j, A, B):
    if (i < A and j < B) or (i >= A and j >= B):
        return '1'
    return '0'


def solve():
    H, W, A, B = read_ints()
    print('\n'.join([
        ''.join([cell(i, j, A, B) for i in range(W)]) for j in range(H)
    ]))



if __name__ == '__main__':
    solve()
