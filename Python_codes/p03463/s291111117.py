import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    tmp = B-A-1

    if not tmp&1:
        print("Borys")
    else:
        print("Alice")


if __name__ == "__main__":
    main()