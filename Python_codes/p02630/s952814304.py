import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = [list(map(int, input().split())) for i in range(Q)]
    Ac = Counter(A)
    ans = 0
    for k, v in Ac.items():
        ans += int(k)*v

    for b,c in L:
        ans -= b*Ac[b]
        ans += c*Ac[b]
        Ac[c] += Ac[b]
        Ac[b] = 0
        print(ans)
        
if __name__ == '__main__':
    main()