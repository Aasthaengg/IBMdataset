

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    Q = [0]*N
    for i in range(N):
        Q[read_int()-1] = i
    max_k = 1
    k = 1
    for i in range(1, N):
        if Q[i] > Q[i-1]:
            k += 1
            max_k = max(max_k, k)
        else:
            k = 1
    return N-max_k


if __name__ == '__main__':
    print(solve())
