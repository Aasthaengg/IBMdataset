import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    
    n = int(str(a) + str(b))
    ans = "No"
    for i in range(1, 100100 + 1):
        if n == i ** 2:
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
