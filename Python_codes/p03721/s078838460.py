# https://atcoder.jp/contests/abc061/tasks/abc061_c
import sys

def main():
    n, k = map(int, input().split())
    ans = [0 for _ in range(10**5+1)]
    for x in sys.stdin.readlines():
        a, b = map(int, x.split())
        ans[a] += b

    cnt = 0
    for i in range(10**5+1):
        cnt += ans[i]
        if cnt >= k:
            print(i)
            exit()

if __name__ == "__main__":
    main()