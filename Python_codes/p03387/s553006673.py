import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C = map(int, input().split())
    ma, mi = max(A,B,C), min(A,B,C)
    if ma*3%2 != (A+B+C)%2:
        ma += 1
    ans = (ma*3-(A+B+C))//2 + (ma*3-(A+B+C))%2
    print(ans)

if __name__ == '__main__':
    main()