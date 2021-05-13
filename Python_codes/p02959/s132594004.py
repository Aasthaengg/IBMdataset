n = int(input())
monster = list(map(int, input().split()))
defeatable = list(map(int, input().split()))
start = sum(monster)
for idx in range(n) :
    if defeatable[idx] <= monster[idx] :
        monster[idx] -= defeatable[idx]
        defeatable[idx] = 0
    else :
        defeatable[idx] -= monster[idx]
        monster[idx] = 0
        if defeatable[idx] <= monster[idx+1] :
            monster[idx+1] -= defeatable[idx]
            defeatable[idx] = 0
        else :
            defeatable[idx] -= monster[idx+1]
            monster[idx+1] = 0
print(start-sum(monster))
