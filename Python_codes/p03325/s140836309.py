# coding: utf-8


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for a in A:
        while a % 2 == 0 and a > 1:
            ans += 1
            a >>= 1

    print(ans)

if __name__ == "__main__":
    main()
