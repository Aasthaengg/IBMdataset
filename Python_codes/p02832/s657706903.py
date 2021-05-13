import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
num = 1
ans = 0
for i in range(n):
    if a[i] != num:
        ans += 1
    else:
        num += 1

if num == 1:
    print(-1)
else:
    print(ans)