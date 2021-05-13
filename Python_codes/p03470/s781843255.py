import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    mochi = set()
    for _ in range(N):
        d = int(input())
        mochi.add(d)
    print(len(mochi))


if __name__ == "__main__":
    main()
