# coding: utf-8


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    ans = sum([A[i] for i in range(3*N-2, N-1, -2)])

    print(ans)

if __name__ == "__main__":
    main()
