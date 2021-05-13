N=int(input())
H=list(map(int,input().split()))

move=0
move_max=0
h_before=0

for h in H:
    if h_before >= h:
        move += 1
    else:
        move = 0
        
    if move_max < move:
        move_max = move
        
    h_before = h
    
print(move_max)