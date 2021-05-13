import sys
input = sys.stdin.readline
def main():
    N = list(input().rstrip())
    ans = 0
    for n in N:
        ans += int(n)
    if ans%9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()