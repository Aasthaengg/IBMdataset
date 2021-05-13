import collections


def solve():

    n = int(input())
    v = list(map(int, input().split()))
    v0 = v[::2]
    v0_counter = collections.Counter(v0).most_common()
    v1 = v[1::2]
    v1_counter = collections.Counter(v1).most_common()

    if v0_counter[0][0] != v1_counter[0][0]:
        print(n - v0_counter[0][1] - v1_counter[0][1])
        exit()
    else:
        if len(v0_counter) == 1 or len(v1_counter) == 1:
            print(n // 2)
            exit()
        else:
            print(n - max(v0_counter[0][1] + v1_counter[1][1], v0_counter[1][1] + v1_counter[0][1]))


if __name__ == '__main__':
    solve()
