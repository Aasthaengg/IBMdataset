import sys

def main():
    X, Y = map(int, sys.stdin.readline().split())
    if X == Y:
        print(-1)
        return
    R = 1
    while True:
        R *= X
        if R >= 10**18:
            print(-1)
            return
        if R % Y != 0:
            print(R)
            return

main()