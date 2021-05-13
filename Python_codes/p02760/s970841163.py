a = []
for i in range(3):
    a.append(list(map(int, input().split())))
n = int(input())

b = []
for i in range(n):
    b.append(int(input()))

card = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if a[j][k] == b[i]:
                card[j][k] = True

yes = "Yes"
no = 'No'

answer = no

for i in range(3):
    if card[0][i] and card[1][i] and card[2][i]:
        answer = yes
for i in range(3):
    if card[i][0] and card[i][1] and card[i][2]:
        answer = yes
if card[0][0] and card[1][1] and card[2][2]:
    answer = yes
if card[0][2] and card[1][1] and card[2][0]:
    answer = yes

print(answer)