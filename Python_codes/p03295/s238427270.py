import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    demand = [tuple(map(int, input().split())) for _ in range(m)]
    demand.sort(key=lambda x: x[1])
    prev_cut = 0
    ans = 0
    for a, b in demand:
        if prev_cut < a:
            ans += 1
            prev_cut = b - 1
    print(ans)


if __name__ == "__main__":
    main()
