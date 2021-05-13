import sys


def resolve(in_):
    n = int(in_.readline())
    h = tuple(map(int, in_.readline().split()))

    answer = [0] * n

    answer[1] = abs(h[1] - h[0])
    for i in range(2, n):
        answer[i] = min(answer[i - 1] + abs(h[i] - h[i - 1]), answer[i - 2] + abs(h[i] - h[i - 2]))
    # print(h, answer)
    return answer[n - 1]


def main():
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()