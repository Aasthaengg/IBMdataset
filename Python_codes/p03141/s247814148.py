

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    AB = []
    for _ in range(N):
        A, B = read_ints()
        AB.append((A+B, A, B))
    AB.sort()
    scores = [0, 0]
    p = 0
    while AB:
        _, *s = AB.pop()
        scores[p] += s[p]
        p ^= 1
    return scores[0]-scores[1]


if __name__ == '__main__':
    print(solve())
