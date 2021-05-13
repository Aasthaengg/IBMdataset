import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    ans = 0
    while a <= b:
        ans += 1
        a *= 2
    print(ans)


if __name__ == "__main__":
    main()