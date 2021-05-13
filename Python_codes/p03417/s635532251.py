import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, m = MI()
    if n == 2 or m == 2:
        print(0)
        sys.exit()
    h = max(n-2, 1)
    w = max(m-2, 1)
    print(h*w)

if __name__ == '__main__':
    main()