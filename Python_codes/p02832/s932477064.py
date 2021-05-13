import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    kk = 1
    for i in a:
        if i == kk:
            kk += 1
        else:
            ans += 1
    print(-1 if ans == n else ans)

if __name__ == '__main__':
    main()
