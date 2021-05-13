import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    num = list(map(int, readline().strip()))

    for bits in range(1 << 3):
        tmp = num[0]
        for i in range(3):
            if bits & (1 << i):
                tmp += num[i + 1]
            else:
                tmp -= num[i + 1]
        if tmp == 7:
            ans = [str(num[0])]
            for i in range(3):
                if bits & (1 << i):
                    ans.append('+')
                else:
                    ans.append('-')
                ans.append(str(num[i + 1]))
            ans.append('=7')
            ans = ''.join(ans)
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
