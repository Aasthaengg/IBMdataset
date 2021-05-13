import sys
# from collections import defaultdict
from collections import Counter
# from queue import Queue
# sys.setrecursionlimit(2000000)

def main():
    N = int(input())
    As = [int(s) for s in input().split()]

    i_plus_As = [(i+1)+As[i] for i in range(N)]
    counter = Counter(i_plus_As)

    ans = 0
    for i in range(N):
        i_value = ( i + 1 )- As[i]
        if i_value <= 0:
            continue

        ans += counter[i_value]

    print(ans)

    return 0

if __name__ == '__main__':
    sys.exit(main())
