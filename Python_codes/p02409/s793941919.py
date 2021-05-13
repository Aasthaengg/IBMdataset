box = [[[0]*10 for i in range(3)] for j in range(4)]
num = int(input())
for i in range(num):
    temp = list(map(int, input().split()))
    box[temp[0]-1][temp[1]-1][temp[2]-1] += temp[3]
    if box[temp[0]-1][temp[1]-1][temp[2]-1] < 0: box[temp[0]-1][temp[1]-1][temp[2]-1] = 0

for i in range(len(box)):
    [print(" "+" ".join( map(str, box[i][j])) ) for j in range(len(box[i]))]
    if i != 3:
        print("####################")