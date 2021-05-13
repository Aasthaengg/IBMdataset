#
# 10c
#
import math


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        s = list(map(int, input().split()))
        m = sum(s) / n
        aan = 0
        for i in range(n):
            aan += (s[i] - m)**2
        print(f"{math.sqrt(aan/n):.4f}")


if __name__ == '__main__':
    main()

