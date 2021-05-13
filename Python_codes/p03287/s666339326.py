import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
        B[i] %= M
    #print(B)
    
    d = defaultdict(int)
    for b in B: d[b] += 1
    #print(d)
    ans = 0
    for m in d: ans += d[m] * (d[m] - 1) // 2
    print(ans)
    

if __name__ == "__main__":
    main()
