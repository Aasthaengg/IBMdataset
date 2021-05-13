import math
import sys
input = sys.stdin.readline


def main():
    N = int(input())

    answer = 0
    for a in range(1, math.ceil(N**(1 / 2))):
        for b in range(a, N):
            c = (N - a * b)
            if c <= 0:
                break
            if a != b:
                answer += 2
            else:
                answer += 1
    print(answer)


if __name__ == "__main__":
    main()
