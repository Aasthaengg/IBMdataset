

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S = input()
    N = len(S)
    base = 1
    remainders = [0]*13
    remainders[0] = 1
    number = 0
    modulo = 10**9+7
    for i in range(N-1, -1, -1):
        new_remainders = [0]*13
        if S[i] == '?':
            for digit in range(10):
                for r in range(len(remainders)):
                    new_remainders[(base*digit+r)%13] += remainders[r]
        else:
            digit = int(S[i])
            for r in range(13):
                new_remainders[(base*digit+r)%13] = remainders[r]
        base = (base*10)%13
        remainders = [r%modulo for r in new_remainders]
    return remainders[5]


if __name__ == '__main__':
    print(solve())
