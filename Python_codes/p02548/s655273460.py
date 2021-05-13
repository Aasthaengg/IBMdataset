import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for i in range(1, N):
        ans += (N-1)//i
    print(ans)

if __name__ == '__main__':
    main()