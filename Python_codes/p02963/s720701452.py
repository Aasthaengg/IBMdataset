import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

MOD = 1000000007

def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b

def main():
    S = int(readline())
    if S!=10**18:
        a = S%1000000000
        b = S//1000000000
        x1 = 1000000000
        y2 = b
        x2 = a
        y1 = -1
        print(0,1,x1,1+y1,x2,1+y2)
    else:
        print(0,0,1000000000,0,0,1000000000)


if __name__ == '__main__':
    main()