import sys
def input(): return sys.stdin.readline().strip()


def main():
    X = [int(input()) for _ in range(4)]
    print(min(X[:2]) + min(X[2:]))



if __name__ == "__main__":
    main()
