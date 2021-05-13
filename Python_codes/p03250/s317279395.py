import sys

input = sys.stdin.readline


def main():
    A, B, C = input().split()

    ans = max(int(A + B) + int(C), int(B + C) + int(A), int(C + A) + int(B))

    print(ans)


if __name__ == "__main__":
    main()
