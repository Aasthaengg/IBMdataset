from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    e = 0
    o = 0
    for v in c.values():
        if v % 2 == 0:
            e += 1
        else:
            o += 1
    if e % 2 != 0:
        e -= 1
    print(o + e)


if __name__ == '__main__':
    main()
