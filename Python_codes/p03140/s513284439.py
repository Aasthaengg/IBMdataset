from collections import Counter


def main():
    n = int(input())
    a = input()
    b = input()
    c = input()

    cnt = 0
    for es in zip(a, b, c):
        ec = Counter(es)
        l = len(ec)
        if l == 3:
            cnt += 2
        elif l == 2:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
