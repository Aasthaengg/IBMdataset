import sys
def input(): return sys.stdin.readline().strip()

def main():
    W, a, b = map(int, input().split())
    if a + W < b:
        print(b - a - W)
    elif a < b + W:
        print(0)
    else:
        print(a - b - W)


if __name__ == "__main__":
    main()
