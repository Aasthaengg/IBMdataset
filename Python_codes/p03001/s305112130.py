import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    w, h, x, y = MI()
    s = h*w*0.5
    flag = int(x == 0.5*w and y == 0.5*h)
    print("{} {}".format(s, flag))
if __name__ == '__main__':
    main()