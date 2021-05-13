import sys
input = sys.stdin.readline


def main():
    S = input().strip()
    import itertools
    for a in itertools.product(["", "A"], repeat=4):
        s = a[0] + "KIH" + a[1] + "B" + a[2] + "R" + a[3]
        if S == s:
            print("YES")
            return
    print("NO")


if __name__ == '__main__':
    main()
