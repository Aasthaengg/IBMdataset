

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    S = input().strip()
    ans = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            ans += 1
    return ans


if __name__ == '__main__':
    print(solve())
