

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    O = input().strip()
    E = input().strip()
    answer = [None]*(len(O)+len(E))
    for i in range(len(O)):
        answer[2*i] = O[i]
    for i in range(len(E)):
        answer[2*i+1] = E[i]
    return ''.join(answer)


if __name__ == '__main__':
    print(solve())
