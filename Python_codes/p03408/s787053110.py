import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    s = [input() for _ in range(n)]
    m = I()
    t = [input() for _ in range(m)]
    word = set(s) | set(t)
    ans = 0
    for w in word:
        cnt = s.count(w)
        cnt -= t.count(w)
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()