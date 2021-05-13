

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    '''
    RL...LL 0
    RL...RR 0
    RL...RL 0

    RL...LR +2
    LR...RL +2

    RL      +1

    13 3
    LRRLRLRRLRLLR
    '''
    N, K = read_ints()
    S = input()
    score = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            score += 1
    return min(score+2*K, N-1)


if __name__ == '__main__':
    print(solve())
