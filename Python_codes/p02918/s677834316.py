import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    s = list(input())
    cnt = 0  # 幸福の人の数
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    # 1回の操作で最大２人まで幸福にできるが，必ず一人は幸福にならない
    print(min(n-1, cnt + 2 * k))


if __name__ == '__main__':
    main()