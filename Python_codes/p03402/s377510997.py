h2 = 50
w2 = 50
ans = [["." for x in range(w2 * 2)] for y in range(h2 * 2)]

a, b = map(int, input().split())
a -= 1
if a != 0:
    b -= 1

cnt = 0
for y in range(h2):
    for x in range(w2):
        cnt += 1
        if cnt <= a:
            ans[y * 2][x * 2 + 1] = "#"
            ans[y * 2 + 1][x * 2] = "#"
            ans[y * 2 + 1][x * 2 + 1] = "#"
        elif a < cnt <= a + b:
            ans[y * 2 + 1][x * 2 + 1] = "#"


print(h2 * 2, w2 * 2)
for s in ans:
    print("".join(s))