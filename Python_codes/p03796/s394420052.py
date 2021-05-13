import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    mod = int(1e9 + 7)
    n = I()
    p = 1
    for i in range(1, n+1):
        p = (p*i)%mod
    print(p)

if __name__ == '__main__':
    main()