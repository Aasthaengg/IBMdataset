import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    diff_1 = A * B * (C % 2)
    diff_2 = A * (B % 2) * C
    diff_3 = (A % 2) * B * C
    
    ans = min(diff_1, diff_2, diff_3)
    print(ans)


if __name__ == "__main__":
    main()
