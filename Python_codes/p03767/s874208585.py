import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

cnt = 0
ans = 0
for i in range(len(a)):
    if i % 2 == 1:
        ans += a[i]
        cnt += 1
    if cnt == n:
        break
print(ans)
