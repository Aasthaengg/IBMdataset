import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    x = I()
    ans = (x//11)*2
    t = x%11
    if t == 0:
        pass
    elif t >= 1 and t <= 6:
        ans += 1
    else:
        ans += 2
    print(ans)

if __name__ == '__main__':
    main()