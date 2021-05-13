import sys
import copy


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    ls = [0] * 50
    for v in a:
        s = bin(v)[2:]
        for i in range(len(s)):
            if s[-i-1] == "1":
                ls[i] += 1
    ans = ["0"] * 50
    for i in range(len(ls)):
        if ls[-i-1] <= n // 2:
            ans[i] = "1"
            t = copy.deepcopy(ans)
            if k < int("".join(t), 2):
                ans[i] = "0"
    t = 0
    for v in a:
        t += int("".join(ans), 2) ^ v
    print(t)


if __name__ == '__main__':
    solve()
