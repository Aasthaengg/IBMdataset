import sys
from collections import defaultdict, Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    H, W = in_nn()
    a = []
    for i in range(H):
        a += list(in_s())

    mH = -(-H // 2)
    mW = -(-W // 2)
    nums = defaultdict(int)
    for y in range(mH):
        for x in range(mW):
            if x == W - x - 1 and y == H - y - 1:
                n = 1
            elif x == W - x - 1:
                n = 2
            elif y == H - y - 1:
                n = 2
            else:
                n = 4
            nums[n] += 1

    count = Counter(a)
    td = defaultdict(int)
    for v in count.values():
        for n in (4, 2, 1):
            if v >= n:
                if td[n] < nums[n]:
                    c = min(v // n, nums[n] - td[n])
                    td[n] += c
                    v -= n * c

    # print(nums)
    # print(td)

    ans = 'Yes'
    for n in (4, 2, 1):
        if td[n] != nums[n]:
            ans = 'No'
            break

    print(ans)


if __name__ == '__main__':
    main()
