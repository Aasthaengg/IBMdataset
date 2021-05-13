import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    trans = [I(), I(), I(), I(), I()]
    ans = 0
    if n%min(trans) == 0:
        ans = n//min(trans) + 4
    else:
        ans = n//min(trans) + 5
    print(ans)

if __name__ == '__main__':
    main()