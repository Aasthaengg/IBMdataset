h,w,k = map(int, input().split())
data = [list(input()) for _ in range(h)]

color = 1
ans = []
for i in range(h):
    ans_i = []
    if data[i].count("#") == 0:
        ans.append(ans_i)
        continue
    check = False
    for j in range(w):
        if data[i][j] == "#":
            if check:
                color += 1
            check = True
        ans_i.append(color)
    ans.append(ans_i)
    color += 1

left = 0
for i in range(h):
    if len(ans[i]):
        for j in range(left,i):
            ans[j] = ans[i]
        left = i + 1

for i in range(left,h):
    ans[i] = ans[left-1]

for i in range(h):
    print(*ans[i])