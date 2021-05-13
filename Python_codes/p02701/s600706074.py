import sys
input = sys.stdin.readline


def main():
    n = int(input())
    items = {input().rstrip() for _ in range(n)}
    print(len(items))


if __name__ == "__main__":
    main()