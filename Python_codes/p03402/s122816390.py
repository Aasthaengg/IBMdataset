White, Black = map(int, input().split())

White -= 1
Black -= 1
# White = "."
# Black = "#"
W = "."
B = "#"

ans = []
for i in range(max(2 * (-(-1 * White // 50)), 2)):
    ans.append([B for i in range(100)])
for j in range(max(2 * (-(-1 * Black // 50)), 2)):
    ans.append([W for i in range(100)])

# print(ans)
tmp = -2
row = 0
while(White != 0):
    if(tmp == 98):
        row += 2
        tmp = 0
    else:
        tmp += 2

    ans[row][tmp] = W
    White -= 1

row += 3
tmp = -2
while(Black != 0):
    # print(row, tmp)
    if(tmp == 98):
        # print(row)
        row += 2
        tmp = 0
    else:
        tmp += 2

    ans[row][tmp] = B
    Black -= 1

print(len(ans), 100)
for a in ans:
    print("".join(a))