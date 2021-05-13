N = int(input())
xl = [list(map(int, input().split())) for _ in range(N)]

XL = [[x-l, x+l] for x,l in xl]
XL.sort(key=lambda x: x[1])

now = -float("inf")
ans = 0
for left, right in XL:
    if now <= left:
        now = right
        ans += 1
print(ans)
