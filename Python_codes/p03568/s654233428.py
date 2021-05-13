import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    A = list(map(int, input().split()))
    allB = 3**n
    exc = 1
    for i in range(n):
        if A[i]%2 == 0:
            exc *= 2
    ans = allB - exc
    print(ans)

if __name__ == '__main__':
    main()