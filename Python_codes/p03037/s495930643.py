import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, m = MI()
    l, r = MI()
    for _ in range(m-1):
        li, ri = MI()
        l = max(l, li)
        r = min(r, ri)
    ans = max(0, r-l+1)
    print(ans)

if __name__ == '__main__':
    main()