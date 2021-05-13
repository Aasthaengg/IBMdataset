import sys
input = sys.stdin.readline
def main():
    A, B = map(int, input().split())
    ans = 0
    for i in range(2):
        ans += max(A,B)
        B = min(A,B)
        A = ans - 1
    print(ans)

if __name__ == '__main__':
    main()