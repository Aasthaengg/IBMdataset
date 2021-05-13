import sys
def input(): return sys.stdin.readline().strip()

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))


if __name__ == "__main__":
    main()
