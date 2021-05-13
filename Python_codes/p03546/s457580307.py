import sys
from collections import defaultdict
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    """
    備忘録としてワ―シャルフロイドによる実装も試してみる。
    wikipediaの解説が意外とわかりやすい？
    """
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    
    d = defaultdict(int)
    for _ in range(H):
        A = list(map(int, input().split()))
        for a in A: d[a] += 1
    ans = 0
    for i in range(10): ans += C[i][1] * d[i]
    print(ans)


if __name__ == "__main__":
    main()
