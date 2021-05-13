import sys

input = sys.stdin.readline

def main():
    ans = 1
    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = [False]*n
    now = a[0]
    c[0] = True
    while now != 2:
        now = a[now-1]
        if c[now-1] == True:
            ans = -1
            break
        ans += 1
        c[now-1] = True
    print(ans)

if __name__ == '__main__':
    main()