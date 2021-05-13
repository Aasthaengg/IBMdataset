import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    for i in range(1, n + 1):
        num = n // i
        ans += ((num * i) + i) * num // 2
    print(ans)

if __name__ == '__main__':
    main()