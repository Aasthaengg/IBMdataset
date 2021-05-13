import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    if a <= b: print(a)
    else: print(a - 1)

if __name__ == "__main__":
    main()
