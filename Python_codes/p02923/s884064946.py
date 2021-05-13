import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
ans = 0
l = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        l += 1
    else:
        ans = max(ans, l)
        l = 0
ans = max(ans, l)
print(ans)