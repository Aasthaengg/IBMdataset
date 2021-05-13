import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

def main():
    H = int(input().strip())
    W = int(input().strip())
    N = int(input().strip())
    ans = N // max(H, W)
    if N % max(H, W) > 0:
        ans += 1
    return ans

if __name__ == "__main__":
    print(main())