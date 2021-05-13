
H,W = map(int,input().split())

lst = [str(input()) for _ in range(H)]

#print(lst)

def check(y,x):
    if x < 0 or x >= W or y < 0 or y >= H:
        return 0
    elif lst[y][x] == '#':
        return 1
    else:
        return 0


fin = [[] for _ in range(H)]
for j in range(H):
    for i in range(W):
    
        sol = 0
        if lst[j][i] == '#':
            sol = '#'
        else:
            
            sol += check(j-1,i)
            sol += check(j+1,i)
            sol += check(j,i-1)
            sol += check(j,i+1)
            sol += check(j-1,i-1)
            sol += check(j+1,i+1)
            sol += check(j+1,i-1)
            sol += check(j-1,i+1)
        fin[j].append(str(sol))    
    print(*fin[j],sep = '')