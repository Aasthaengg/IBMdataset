import math


def main():
    n, k = map(int, input().split())
    As = list(map(int, input().split()))
    ans = math.ceil((n-1)/(k-1))
    print(ans)


if __name__ == "__main__":
    main()
