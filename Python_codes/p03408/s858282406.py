from collections import defaultdict


def main():

    blue = defaultdict(int)
    red = defaultdict(int)

    n = int(input())
    for i in range(n):
        blue[input()] += 1

    m = int(input())
    for i in range(m):
        red[input()] += 1

    ans = 0

    for word, cnt in blue.items():
        if word in red.keys():
            ans = max(ans, cnt - red[word])
        else:
            ans = max(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
