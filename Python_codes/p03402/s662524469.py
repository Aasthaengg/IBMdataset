a, b = map(int, input().split())
ans = []
for i in range(50):
    ans.append(["." for i in range(100)])
for i in range(50):
    ans.append(["#" for i in range(100)])

for i in range((a - 1) // 50):
    for j in range(50):
        ans[51 + i * 2][2 * j] = "."
for i in range((a - 1) % 50):
    ans[99][2 * i] = "."
for i in range((b - 1) // 50):
    for j in range(50):
        ans[i * 2][2 * j] = "#"
for i in range((b - 1) % 50):
    ans[48][2 * i] = "#"

print(100, 100)
for i in range(100):
    print("".join(ans[i]))