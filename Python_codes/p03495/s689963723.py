import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_cnt = sorted(list(Counter(a).values()))
    s = set(a)
    t = max(0, len(s) - k)
    print(sum(a_cnt[0:t]))

if __name__ == '__main__':
    main()