H,W = map(int,input().split())
grid = [[0]*W for _ in range(H)]
for i in range(H):
    grid[i] = list(map(int, input().split()))

done = [[0]*W for _ in range(H)]

def nex(y,x):
    for new_y,new_x in [[y,x+1],[y+1,x],[y-1,x],[y,x-1]]:
        if 0<=new_y<H and 0<=new_x<W and not done[new_y][new_x]:
            return [new_y,new_x]
    return False

ans_ls = []
y,x = 0,0
if grid[y][x] % 2 == 1:
    previous_y, previous_x = y,x
    have_odd = True
else:
    have_odd = False

while True:
    if not nex(y,x):
        break
    y,x  = nex(y,x)
    done[y][x] = 1
    
    # 奇数をもった状態での移動
    if have_odd:
        if grid[y][x] % 2 == 1:
            ans_ls.append([y+1,x+1,previous_y+1,previous_x+1])
            have_odd = False
        else:
            ans_ls.append([y+1,x+1,previous_y+1,previous_x+1])
            previous_y,previous_x = y,x
    # 奇数を持っていない状態での移動
    else:
        if grid[y][x] % 2 == 1:
            previous_y,previous_x = y,x 
            have_odd = True
        else:
            pass

print(len(ans_ls))
for ans in ans_ls:
    print(*ans)