N,M=map(int,input().split())

lands=[False for _ in range(N-1)]
goal_land=[]

for _ in range(M):
    a,b = map(int,input().split())
    if a == 1 or b == 1:
        if a == 1:
            lands[b-1] = True
        else:
            lands[a-1] = True
    elif a == N or b == N:
        if a == N:
            goal_land.append(b-1)
        else:
            goal_land.append(a-1)

#print(lands)
#print(goal_land)

for i in goal_land:
    if lands[i]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')