import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    k = int(input())
    x = list(map(int, input().split()))
    for i in range(n):
        temp = min(x[i], abs(k-x[i]))
        ans += temp*2 
    print(ans)

if __name__ == '__main__':
    main()