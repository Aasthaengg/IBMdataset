import sys
import collections

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    s = [input().rstrip('\n') for _ in range(n)]
    m = int(input())
    t = [input().rstrip('\n') for _ in range(m)]
    cs = collections.Counter(s)
    ct = collections.Counter(t)
    for k,v in cs.items():
        ans = max(v-ct[k], ans)
    print(ans)

if __name__ == '__main__':
    main()