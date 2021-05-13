n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

ans = "No"
for i in range(n - 2):
    bl = True
    for j in range(3):
        bl = bl and (d[i+j][0] == d[i+j][1])

    if bl:
        ans = "Yes"

print(ans)
