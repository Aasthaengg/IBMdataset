import collections


def main():
    n, h, w = map(int, input().split())
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        if h <= a and w <= b:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
