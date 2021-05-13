import sys

input = sys.stdin.readline

def main():
    ans = 0
    n, m = map(int, input().split())
    all = []
    for i in range(n):
        all.append(list(map(int, input().split())))
    all.sort()
    for a,b in all:
        if m >= b:
            m -= b
            ans += a*b
        else:
            ans += a*(m)
            break
    print(ans)

if __name__ == '__main__':
    main()