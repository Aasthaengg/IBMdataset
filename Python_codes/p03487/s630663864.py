import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(input().split())
    C = Counter(A)
    ans = 0
    for k, v in C.items():
        if v >= int(k):
            ans += v - int(k)
        else:
            ans += v
    print(ans)

if __name__ == '__main__':
    main()