import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    K, X = read_values()
    print("Yes" if X <= K * 500 else "No")


if __name__ == "__main__":
    main()
