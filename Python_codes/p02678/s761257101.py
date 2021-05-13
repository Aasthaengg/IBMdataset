from collections import defaultdict
import sys
room_num,root_num = map(int,input().split())
#room_dis_dic = dict(zip(range(1,room_num+1),[0]+[sys.maxsize]*(room_num-1)))
connect_dic = defaultdict(set)
connected_list = [1]
next_connect_dic = {}
for _ in range(root_num):
    a,b = map(int,input().split())
    connect_dic[a].add(b)
    connect_dic[b].add(a)
    
for room_i in connected_list:
    #print(room_i)
    next_room_set = {connect_to for connect_to in connect_dic[room_i] if connect_to not in next_connect_dic.keys()}
    connected_list.extend(list(next_room_set))
    for next_room_i in next_room_set:
        next_connect_dic[next_room_i] = room_i

if len(set(range(2,room_num+1))-next_connect_dic.keys())!=0:
    print("No")
else:
    print("Yes")
    for i in range(2,room_num+1):
        print(next_connect_dic[i])