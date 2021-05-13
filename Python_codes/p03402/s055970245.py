a, b = map(int, input().split())

print(100, 100)

ans = [["" for i in range(100)] for j in range(100)]
for i in range(50):
    for j in range(100):
        ans[i][j] = "."
for i in range(50, 100):
    for j in range(100):
        ans[i][j] = "#"

a -= 1
b -= 1

for i in range(0, 49, 2):
    for j in range(100):
        if b == 0:
            break
        if (i+j) % 2 == 0:
            ans[i][j] = "#"
            b -= 1
    else:
        continue
    break

for i in range(51, 100, 2):
    for j in range(100):
        if a == 0:
            break
        if (i+j) % 2 == 1:
            ans[i][j] = "."
            a -= 1
    else:
        continue
    break

tans = ["" for i in range(100)]
for i in range(100):
    for j in range(100):
        tans[i] += ans[i][j]

for i in range(100):
    print(tans[i])