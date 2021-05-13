import sys
input = sys.stdin.readline


def main():
    mod = 10**9 + 7
    x = int(input())
    counts = [0] * (x+1)
    counts[0] = 1
    for i in range(x-2):
        for num in range(3, x-i+1):
            counts[i+num] += counts[i]
            counts[i+num] %= mod

    print(counts[x])


if __name__ == "__main__":
    main()
