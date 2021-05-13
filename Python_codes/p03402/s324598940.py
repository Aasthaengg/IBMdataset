a, b = map(int, input().split())
ans = []
for i in range(50):
    ans.append(["."] * 100)
for i in range(50):
    ans.append(["#"] * 100)

i = 0
b -= 1
while b > 0:
    for j in range(0, 100, 2):
        ans[i][j] = "#"
        b -= 1
        if b == 0:
            break
    i += 2

i = 60
a -= 1
while a > 0:
    for j in range(0, 100, 2):
        ans[i][j] = "."
        a -= 1
        if a == 0:
            break
    i += 2
print(100, 100)
for i in range(100):
    print("".join(ans[i]))
