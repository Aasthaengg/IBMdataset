import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    K = int(input())
    X = list(map(int, input().split()))
    ans = 0
    for i, x in enumerate(X):
        ans += min(abs(x), abs(x - K))
    print(ans * 2)
    


if __name__ == "__main__":
    main()
