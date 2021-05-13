H, W = map(int, input().split())

A = []

for i in range(H):
    A.append(list(map(int, input().split())))
    
ans_loc = []
ans_count = 0

for i in range(H):
    for j in range(W):
        if i == H-1 and j == W-1:
            break
        elif i%2 == 0:
            x = j
            y = i
            if j == W-1:
                x_d = 0
                y_d = 1
            else:
                x_d = 1
                y_d = 0
             
        else:
            x = (W-j-1)
            y = i
            if j == W-1:
                x_d = 0
                y_d = 1
            else:
                x_d = -1
                y_d = 0
                
        if A[y][x]%2 == 1:
            A[y][x] -= 1
            A[y+y_d][x+x_d] += 1
            ans_loc.append((y+1,x+1,y+y_d+1,x+x_d+1))
            ans_count += 1

print(ans_count)

for i in ans_loc:
    print(' '.join(map(str, i)))
            
            


