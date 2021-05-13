import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    for i in range(A, B+1):
        s = str(i)
        if s == s[::-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()