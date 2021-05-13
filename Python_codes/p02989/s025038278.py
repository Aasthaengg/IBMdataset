# coding: utf-8

def main():
    N = int(input())
    d = sorted(list(map(int, input().split())))
    ans = 0
    if d[N // 2] != d[N // 2 - 1]:
        ans = d[N // 2] - d[N // 2 - 1]

    print(ans)


if __name__ == "__main__":
    main()
