import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    title = defaultdict(int)
    cumsum = [0]
    for i in range(1, N + 1):
        s, t = readline().strip().decode('utf-8').split()
        title[s] = i
        cumsum.append(cumsum[-1] + int(t))
    X = readline().decode('utf-8').strip()
    ans = cumsum[-1] - cumsum[title[X]]
    print(ans)


if __name__ == '__main__':
    main()
