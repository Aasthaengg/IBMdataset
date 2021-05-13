c = []
for i in range(3):
    li = list(map(int, input().split()))
    c.append(li)

a = [0, (c[1][0]-c[0][0]),(c[2][0]-c[0][0]) ]
b = [c[0][0], c[0][1], c[0][2]]
ans = "Yes"

for i in range(3):
    for j in range(3):
        if c[i][j] == (a[i] + b[j]):
            pass
        else:
            ans = "No"
            break
    if ans == "No":
        break

print(ans)