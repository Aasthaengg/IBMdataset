import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readline_s = sys.stdin.readline
readlines = sys.stdin.buffer.readlines


def main():

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if abs(a - e) <= k:
        ans = 'Yay!'
    else:
        ans = ':('

    print(ans)


if __name__ == '__main__':
    main()
