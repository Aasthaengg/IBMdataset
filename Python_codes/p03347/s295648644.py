import sys
input = sys.stdin.readline

n = int(input())
pre = -1
ans = -1
for i in range(n):
    a = int(input())
    if a > i or a > pre + 1:
        print(-1)
        exit()

    if a <= pre:
        ans += a
    else:
        ans += 1
    pre = a

print(ans)