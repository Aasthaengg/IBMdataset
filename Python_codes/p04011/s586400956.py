import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    k = I()
    x = I()
    y = I()
    if n <= k:
        print(n*x)
    else:
        print(k*x + (n-k)*y)

if __name__ == '__main__':
    main()