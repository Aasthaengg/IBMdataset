import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    if N >= 1000: print("ABD")
    else: print("ABC")


if __name__ == "__main__":
    main()
