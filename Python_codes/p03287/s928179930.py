import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a[0] = a[0]%m
    for i in range(1, n):
        a[i] += a[i-1]
        a[i] %= m
    a.sort()
    target = 0
    cnt = 1
    for i in a:
        if i == target:
            ans += cnt
            cnt += 1
        else:
            target = i
            cnt = 1
    print(ans)

if __name__ == "__main__":
    main()