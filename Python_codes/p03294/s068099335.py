# coding: utf-8


def main():
    N = int(input())
    ans = sum(list(map(int, input().split()))) - N
    print(ans)

if __name__ == "__main__":
    main()
