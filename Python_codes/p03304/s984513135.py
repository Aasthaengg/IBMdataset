import sys
def main():
    input = sys.stdin.readline
    n,m,d = map(int, input().split())

    n_ud = max(0, n-2*d)
    ud = 2 if d != 0 else 1
    ans = 0
    for i in range(m-1):
        ans += n_ud*ud + (n-n_ud)
    print(ans/n/n)

if __name__ == '__main__':
    main()