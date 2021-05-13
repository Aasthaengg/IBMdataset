import sys

if __name__ == "__main__":
    N = int(input())
    X = []
    for _ in range(N):
        x, l = [int(x) for x in input().split(" ")]
        X.append((x - l, x + l))

    X.sort(key=lambda x: x[1])

    count = 0
    max_high = -sys.maxsize
    for low, high in X:
        if max_high <= low:

            count += 1
            max_high = high
    print(count)
