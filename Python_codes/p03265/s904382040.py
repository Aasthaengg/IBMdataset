import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    x1, y1, x2, y2 = MI()
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x3 - x2 + x1
    y4 = y3 - y2 + y1
    print("{} {} {} {}".format(x3, y3, x4, y4))

if __name__ == '__main__':
    main()