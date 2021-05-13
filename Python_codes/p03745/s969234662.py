import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
ans = 1
# 増加or減少
check = 0
before = a[0]
for i in a[1:]:
    if i == before:
        continue
    if before > i:
        if check == 0:
            check = 1
        elif check == -1:
            ans += 1
            check = 0
    else:
        if check == 0:
            check = -1
        elif check == 1:
            ans += 1
            check = 0
    before = i

print(ans)
