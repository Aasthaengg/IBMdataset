from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))

main()