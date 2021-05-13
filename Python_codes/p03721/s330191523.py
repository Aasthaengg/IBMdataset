from collections import defaultdict
import sys
buf = sys.stdin.buffer


def main():
    n, k = map(int, buf.readline().split())
    AB = map(int, buf.read().split())

    count = defaultdict(int)
    for a, b in zip(AB, AB):
        count[a] += b

    idx = 0
    for num in sorted(count.keys()):
        idx += count[num]
        if idx >= k:
            print(num)
            break


if __name__ == "__main__":
    main()
