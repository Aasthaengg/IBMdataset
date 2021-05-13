import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        for j in range(i, i+2):
            if a[j] >= b[i]:
                a[j] -= b[i]
                ans += b[i]
                break
            else:
                ans += a[j]
                b[i] -=  a[j]
                a[j] = 0
    print(ans)

if __name__ == '__main__':
    main()