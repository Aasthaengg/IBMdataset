import sys
input = sys.stdin.readline

def main():
    X, Y = map(int, input().split())
    ans = 0
    t = [300000, 200000, 100000]

    if X <= 3:
        ans += t[X-1]
    if Y <= 3:
        ans += t[Y-1]
    if X == 1 and Y == 1:
        ans += 400000
    
    print(ans)

if __name__ == "__main__":
    main()