import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, d = map(int, input().split())
    tree = 1
    ans = 0
    while True:
        ans += 1
        tree += 2 * d
        if tree >= n:
            print(ans)
            return
        tree += 1

if __name__ == '__main__':
    main()