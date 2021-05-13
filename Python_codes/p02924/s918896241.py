import sys

input = sys.stdin.readline

def main():
    n = int(input())-1
    ans = (1+n)*(n//2)
    if n%2 != 0:
        ans += n//2+1
    print(ans)

if __name__ == '__main__':
    main()