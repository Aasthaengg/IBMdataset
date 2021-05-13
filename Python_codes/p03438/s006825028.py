import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    n = sum(B) - sum(A)
    if n < 0:
        print("No")
        exit()

    n_need = 0
    for a, b in zip(A, B):
        if a > b:
            n_need += (a - b)
        elif a < b:
            n_need += (b - a) % 2

    ans = "Yes" if n_need <= n else "No"
    print(ans)


if __name__ == "__main__":
    main()
