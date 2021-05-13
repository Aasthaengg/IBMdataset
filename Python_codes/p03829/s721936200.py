
from collections import defaultdict
import sys


def main():
    num, move, telepote = map(int, input().split())
    data = list(map(int, input().split()))

    ans = 0
    for i in range(num - 1):
        ans += min(telepote, move * (data[i + 1] - data[i]))

    print(ans)



if __name__ == '__main__':
    main()
