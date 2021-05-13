import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readline_s = sys.stdin.readline
readlines = sys.stdin.buffer.readlines


def main():

    num = []
    for i in range(5):
        num.append(int(readline()))

    k = 99
    ind = -1
    for i in range(5):
        r = num[i] % 10
        if r != 0:
            if r < k:
                k = r
                ind = i

    ans = 0
    for i in range(5):
        if i == ind:
            ans += num[i]
        else:
            ans += 10 * ((num[i] - 1) // 10 + 1)

    print(ans)


if __name__ == '__main__':
    main()
