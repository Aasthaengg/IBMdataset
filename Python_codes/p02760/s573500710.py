card = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
check = [int(input()) for _ in range(n)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if card[i][j] == check[k]:
                card[i][j] = 0

ans = "No"
for i in range(3):
    if card[i][0] + card[i][1] + card[i][2] == 0:
        ans = "Yes"
    if card[0][i] + card[1][i] + card[2][i] == 0:
        ans = "Yes"

if card[0][0] + card[1][1] + card[2][2] == 0:
    ans = "Yes"
if card[0][2] + card[1][1] + card[2][0] == 0:
    ans = "Yes"
print(ans)