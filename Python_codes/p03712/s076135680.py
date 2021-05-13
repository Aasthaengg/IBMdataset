import sys

input = sys.stdin.readline

def main():
    ans = ''
    f = '#'
    n = '\n'
    H, W = map(int, input().split())
    ans += f*(W+2)
    for _ in range(H):
        ans += n + f + input().rstrip(n) + f
    ans += n + f*(W+2)
    print(ans)

if __name__ == '__main__':
    main()