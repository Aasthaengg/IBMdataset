import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readline_s = sys.stdin.readline
readlines = sys.stdin.buffer.readlines


def main():

    N = int(readline())
    num = []
    for i in range(5):
        num.append(int(readline()))

    q, r = divmod(N, min(num))
    ans = q + 4
    ans += 1 if r else 0
    print(ans)


if __name__ == '__main__':
    main()
