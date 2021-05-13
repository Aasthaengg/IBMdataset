import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C, K = map(int, input().split())
    if K%2 == 0:
        ans = A - B
    else:
        ans = B - A
    if ans >= 10**18:
        ans = 'Unfair'
    print(ans)

if __name__ == '__main__':
    main()