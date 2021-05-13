# 

H, W = map(int, input().split())
A = []

for i in range(H):
    A.append(list(map(int, input().split())))
    
ans_loc = []

for i in range(H):
    for j in range(W):
        if i == H-1 and j == W-1:
            break
            
        elif A[i][j]%2 == 1:          
            if j == W-1:
                A[i][j] -= 1
                A[i+1][j] += 1
                ans_loc.append((i+1, j+1, i+2, j+1))
            else:
                A[i][j] -= 1
                A[i][j+1] += 1
                ans_loc.append((i+1, j+1, i+1, j+2))
            
print(len(ans_loc))
for i in ans_loc:
    print(' '.join(map(str, i)))
