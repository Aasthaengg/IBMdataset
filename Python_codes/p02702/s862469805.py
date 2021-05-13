import sys

input = sys.stdin.readline
P = 2019


def main():
    S = input().rstrip()

    count = [0] * P
    count[0] += 1
    T = 0
    d = 1
    for s in reversed(S):
        T = (T + int(s) * d) % P
        count[T] += 1
        d = (d * 10) % P

    ans = 0
    for k in count:
        ans += k * (k - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
