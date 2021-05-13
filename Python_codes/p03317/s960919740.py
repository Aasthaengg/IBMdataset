import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, k = MI()
    a = LI()
    ans = -(-(n-1) // (k-1))
    print(ans)

if __name__ == '__main__':
    main()