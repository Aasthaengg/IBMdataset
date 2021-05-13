import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    d, n = MI()
    if n%100 == 0:
        n += 1
    ans = (100**d)*n
    print(ans)

if __name__ == '__main__':
    main()