import sys

input = sys.stdin.readline

def main():
    S = input()
    cnt = S.count('o')
    ans = 700 + cnt * 100
    print(ans)

if __name__ == '__main__':
    main()