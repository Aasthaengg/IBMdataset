import sys

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    w = 0
    for s in S[::-1]:
        if s == 'W':
            w += 1
        else:
            ans += w
    print(ans)

if __name__ == '__main__':
    main()