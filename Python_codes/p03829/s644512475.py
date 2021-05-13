import sys;input = lambda : sys.stdin.readline()
n, a, b = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    d = arr[i] - arr[i - 1]
    ans += min(b, d * a)
print(ans)