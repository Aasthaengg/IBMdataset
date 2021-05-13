N, M = map(int, input().split())

H_list = list(map(int, input().split()))

road_list = []

for i in range(M):
    road = list(map(int, input().split()))
    road_list.append(road)

ans_list = [0 for i in range(N)]

for i in range(M):
    #print(i, road_list[i][0]-1)
    if H_list[road_list[i][0]-1] > H_list[road_list[i][1]-1]:
        ans_list[road_list[i][1]-1] = -1
    elif H_list[road_list[i][0]-1] < H_list[road_list[i][1]-1]:
        ans_list[road_list[i][0]-1] = -1
    elif H_list[road_list[i][0]-1] == H_list[road_list[i][1]-1]:
        ans_list[road_list[i][1]-1] = -1
        ans_list[road_list[i][0]-1] = -1
        
#print(ans_list)    
print(ans_list.count(0))