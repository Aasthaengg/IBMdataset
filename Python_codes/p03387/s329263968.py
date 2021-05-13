import sys
input = sys.stdin.readline
def main():
    num = list(map(int, input().split()))
    MAX = max(num)
    CNT = 0
    for i in range(3):
        num[i] -= MAX
        CNT -= num[i]
    if CNT%2 == 0:
        ans = CNT//2
        print(ans)
    else:
        ans = CNT//2 + 2
        print(ans)

if __name__ == '__main__':
    main()