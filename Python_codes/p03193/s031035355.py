# caddi2018bB - AtCoder Alloy
import sys
input = sys.stdin.readline

def main():
    n, h, w = list(map(int, input().rstrip().split()))
    R = [list(map(int, input().rstrip().split())) for _ in range(n)]
    ans = sum(1 for a, b in R if a >= h and b >= w)
    print(ans)


if __name__ == "__main__":
    main()