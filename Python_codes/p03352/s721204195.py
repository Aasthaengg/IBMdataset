import sys
def input(): return sys.stdin.readline().strip()


def main():
    X = int(input())
    if X < 4:
        print(1)
        return
    ans = 1
    for b in range(2, int(X ** 0.5) + 2):
        for p in range(11):
            if b ** p > X: break
            ans = max(ans, b ** p)
    print(ans)

if __name__ == "__main__":
    main()
