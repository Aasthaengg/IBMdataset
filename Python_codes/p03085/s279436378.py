import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readline_s = sys.stdin.readline
readlines = sys.stdin.buffer.readlines


def main():
    b = readline_s().rstrip()

    if b == 'A':
        ans = 'T'
    elif b == 'T':
        ans = 'A'
    elif b == 'C':
        ans = 'G'
    elif b == 'G':
        ans = 'C'

    print(ans)


if __name__ == '__main__':
    main()
