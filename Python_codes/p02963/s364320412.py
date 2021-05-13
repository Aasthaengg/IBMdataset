import sys
input = sys.stdin.readline

def main():
    S = int(input())
    x1, y1 = 0, 0
    if S <= 10**9:
        x2, y2 = S, 0
        x3, y3 = 0, 1
    else:
        x2, y2 = 10**9, 1
        x3 = (10**9 - S%10**9)%10**9
        y3 = (S+x3)//(10**9)
    print(x1, y1, x2, y2, x3, y3)

if __name__ == '__main__':
    main()