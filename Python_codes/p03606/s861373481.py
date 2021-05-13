import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lr_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for lr in lr_list:
        ans += lr[1] - lr[0] + 1
    print(ans)

if __name__ == '__main__':
    main()
