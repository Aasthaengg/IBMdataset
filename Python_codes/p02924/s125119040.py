import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    if n == 1:
        print(0)
        sys.exit()
    ans = (n*(n-1))//2
    print(ans)

if __name__ == '__main__':
    main()