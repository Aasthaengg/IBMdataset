import queue

h,w = map(int,input().split())
si = [input() for i in range(h)]

q = queue.Queue()

check = [-1]*(h*w)

vx = [0,1,0,-1]
vy = [1,0,-1,0]

for i in range(h*w):
    y = i//w
    x = i%w
    if si[y][x] == '#':
        if check[i] != -1:
            continue
        q.put([i,'#'])
        check[i] = i
        
        while not q.empty():
            num, clr = q.get()
            y = num//w
            x = num%w
            
            for j in range(4):
                ny = y + vy[j]
                nx = x + vx[j]
                if ny >= 0 and ny < h and nx >= 0 and nx < w:
                    new_num = ny*w+nx
                    if check[new_num] != -1:
                        continue
                    #print(new_num)
                    if clr == '#':
                        if si[ny][nx] == '.':
                            q.put([new_num,'.'])
                            check[new_num] = check[num]
                    else:
                        if si[ny][nx] == '#':
                            q.put([new_num,'#'])
                            check[new_num] = check[num]
    
#print(check)

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