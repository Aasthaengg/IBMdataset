import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))

    n_2 = 0
    n_1 = 0
    for a, b in zip(A, B):
        if a > b:
            n_1 += (a - b)
        elif a < b:
            n_2 += (b - a + 1) // 2

    diff = sum(B) - sum(A)
    if n_1 <= diff and n_2 <= diff:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
