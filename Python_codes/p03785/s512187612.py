import sys
n, c, k = map(int, input().split())
a = list(map(int, sys.stdin.readlines()))+[10**10]
a.sort()
ans, cnt, tmp = 0, 1, a[0]+k
for i in a[1:]:
    if i <= tmp and cnt < c:
        cnt += 1
    else:
        tmp, cnt = i + k, 1
        ans += 1

print(ans)