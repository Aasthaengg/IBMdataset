

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def dfs(m, N):
    if N == 0:
        yield []
    else:
        for i in range(0, m+2):
            for solution in dfs(max(m, i), N-1):
                yield [i]+solution

def solve():
    '''
    a
    '''
    N = read_int()
    alphabets = 'abcdefghij'
    for solution in dfs(-1, N):
        print(''.join(alphabets[i] for i in solution))


if __name__ == '__main__':
    solve()
