import sys

sys.setrecursionlimit(10**7)

h,w = map(int,input().split())
si = [input() for i in range(h)]

check = [-1]*(h*w)

#print(check,check==-1)
#exit()

vx = [0,1,0,-1]
vy = [1,0,-1,0]

def dfs(num,clr):
    #print(min(check))
    #if min(check) > -1:
    #    return
    
    y = num//w
    x = num%w
    for j in range(4):
        ny = y + vy[j]
        nx = x + vx[j]
        if ny >= 0 and ny < h and nx >= 0 and nx < w:
            new_num = ny*w+nx
            if check[new_num] != -1:
                continue
            #print(new_num,num,clr,si[ny][nx])
            if clr == '#':
                #print(ny,nx)
                if si[ny][nx] == '.':
                    check[new_num] = check[num]
                    dfs(new_num,'.')
            else:
                    
                if si[ny][nx] == '#':
                    check[new_num] = check[num]
                    dfs(new_num,'#')
            #print(check)

for i in range(h*w):
    #print(i)
    y = i//w
    x = i%w
    if si[y][x] == '#':
        if check[i] != -1:
            continue
        check[i] = i
        dfs(i,'#')
        #print(check)
        #exit()

ans = 0

li = [0]*(h*w+1)

for i in range(h):
    for j in range(w):
        if si[i][j] == '.':
            li[check[i*w+j]] += 1

#print(li)

for i in range(h):
    for j in range(w):
        if si[i][j] == '#':
            ans += li[check[i*w+j]]
            
print(ans)