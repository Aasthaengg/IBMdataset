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
    ans = q + (not (not r)) + 4
    print(ans)


if __name__ == '__main__':
    main()
