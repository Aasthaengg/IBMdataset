import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = input().rstrip('\n')
    c = int(N[0])
    ans = c + 9*(len(N)-1)
    if N[1:]!='9'*(len(N)-1):
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()