dice = list(map(int,input().split()))
x = list(input())

def move(x):
    if x == "N":
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]

    elif x == "W":
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]

    elif x == "E":
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]

    elif x == "S":
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]

for i in range(len(x)):
    move(x[i])
print(dice[0])
