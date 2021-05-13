#069d
H,W = map(int, input().split())
N = int(input())

a_list = [int(e) for e in input().split()]

paint_list = []

for i in range(N):
    paint_list += [i+1 for _ in range(a_list[i])]   

#回答の初期化
ans = []
for i in range(H+2):
    if i==0 or i==H+1:
        ans.append([-1 for _ in range(W+2)])
    else:
        line = [0 for _ in range(W+2)]
        line[0]=-1
        line[W+1]=-1
        ans.append(line)

#回答を埋めていく
x = 1
y = 1
direction = 0

def print_ans():
    for i in range(1,H+1):
        print(' '.join(map(str, ans[i][1:W+1])))

for color in paint_list:
    ans[y][x] = color
    #print_ans()
    #print("")
    
    if direction%4 == 0:
        if ans[y+1][x]==0:
            y += 1
        else:
            direction += 1
            x += 1
    elif direction%4 == 1:
        if ans[y][x+1]==0:
            x += 1
        else:
            direction += 1
            y -= 1
    elif direction%4 == 2:
        if ans[y-1][x]==0:
            y -= 1
        else:
            direction += 1
            x -= 1
    elif direction%4 == 3:
        if ans[y][x-1]==0:
            x -= 1
        else:
            direction += 1
            y += 1

print_ans()