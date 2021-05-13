import sys

input = sys.stdin.readline
N = int(input())

pre = int(input())
if pre != 0:
    print(-1)
    sys.exit()
ans = 0
for _ in range(N-1):
    x = int(input())
    if pre + 1 < x:
        print(-1)
        sys.exit()
    elif pre + 1 == x:
        ans += 1
    else:
        ans += x
    pre = x

print(ans)