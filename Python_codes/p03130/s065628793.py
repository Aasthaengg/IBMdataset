import sys

input = sys.stdin.readline


def main():
    count = [0, 0, 0, 0]
    for _ in range(3):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        count[a] += 1
        count[b] += 1

    if count.count(1) == 2 and count.count(2) == 2:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
