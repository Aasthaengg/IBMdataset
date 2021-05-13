

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    K, S = read_ints()
    # X+Y+Z = S
    # 0 <= X,Y,Z <= K
    total = 0
    for X in range(K+1):
        if S-X < 0:
            break
        # Y+Z=S-X
        Y_min = max(S-X-K, 0)
        Y_max = min(S-X, K)
        if Y_min <= Y_max:
            total += Y_max-Y_min+1
    return total


if __name__ == '__main__':
    print(solve())
