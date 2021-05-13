import sys

input = sys.stdin.readline

def main():
    N = int(input())
    Z = []; W = []
    for i in range(N):
        x, y = map(int, input().split())
        z = x + y
        w = x - y
        Z.append(z)
        W.append(w)
    ans = max(max(Z) - min(Z), max(W) - min(W))
    print(ans)

if __name__ == "__main__":
    main()
