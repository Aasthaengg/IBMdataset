import sys
input=sys.stdin.readline

N,K,L=map(int,input().split())

pq=[list(map(int,input().split())) for _ in range(K)]
rs=[list(map(int,input().split())) for _ in range(L)]

city_road_train=set()

city_roadgroup_dict={}
roadgroup_city_dict={}

city_traingroup_dict={}
traingroup_city_dict={}

for ch_pq in pq:

  if not ch_pq[0] in city_roadgroup_dict:
    if not ch_pq[1] in city_roadgroup_dict:
      new_group_num=ch_pq[0]
      city_roadgroup_dict[ch_pq[0]]=new_group_num
      city_roadgroup_dict[ch_pq[1]]=new_group_num
      roadgroup_city_dict[new_group_num]=set([ch_pq[0],ch_pq[1]])
    else:
      group_num=city_roadgroup_dict[ch_pq[1]]
      city_roadgroup_dict[ch_pq[0]]=group_num
      roadgroup_city_dict[group_num].add(ch_pq[0])
  else:
    if not ch_pq[1] in city_roadgroup_dict:
      group_num=city_roadgroup_dict[ch_pq[0]]
      city_roadgroup_dict[ch_pq[1]]=group_num
      roadgroup_city_dict[group_num].add(ch_pq[1])
    else:
      group_num_0=city_roadgroup_dict[ch_pq[0]]
      group_num_1=city_roadgroup_dict[ch_pq[1]]
      if group_num_0!=group_num_1:
        group_0=roadgroup_city_dict[group_num_0]
        group_1=roadgroup_city_dict[group_num_1]
        if len(group_0)<len(group_1):
          for city_n in list(group_0):
            city_roadgroup_dict[city_n]=group_num_1
          roadgroup_city_dict[group_num_1]|=group_0
          del roadgroup_city_dict[group_num_0]

        else:
          for city_n in list(group_1):
            city_roadgroup_dict[city_n]=group_num_0
          roadgroup_city_dict[group_num_0]|=group_1
          del roadgroup_city_dict[group_num_1]


for ch_rs in rs:
  for rs_i in range(2): 
    if not ch_rs[rs_i] in city_road_train and ch_rs[rs_i] in city_roadgroup_dict:
      city_road_train.add(ch_rs[rs_i])
  
  if not ch_rs[0] in city_traingroup_dict:
    if not ch_rs[1] in city_traingroup_dict:
      new_group_num=ch_rs[0]
      city_traingroup_dict[ch_rs[0]]=new_group_num
      city_traingroup_dict[ch_rs[1]]=new_group_num
      traingroup_city_dict[new_group_num]=set([ch_rs[0],ch_rs[1]])
    else:
      group_num=city_traingroup_dict[ch_rs[1]]
      city_traingroup_dict[ch_rs[0]]=group_num
      traingroup_city_dict[group_num].add(ch_rs[0])
  else:
    if not ch_rs[1] in city_traingroup_dict:
      group_num=city_traingroup_dict[ch_rs[0]]
      city_traingroup_dict[ch_rs[1]]=group_num
      traingroup_city_dict[group_num].add(ch_rs[1])
    else:
      group_num_0=city_traingroup_dict[ch_rs[0]]
      group_num_1=city_traingroup_dict[ch_rs[1]]
      if group_num_0!=group_num_1:
        group_0=traingroup_city_dict[group_num_0]
        group_1=traingroup_city_dict[group_num_1]
        if len(group_0)<len(group_1):
          for city_n in list(group_0):
            city_traingroup_dict[city_n]=group_num_1
          traingroup_city_dict[group_num_1]|=group_0
          del traingroup_city_dict[group_num_0]

        else:
          for city_n in list(group_1):
            city_traingroup_dict[city_n]=group_num_0
          traingroup_city_dict[group_num_0]|=group_1
          del traingroup_city_dict[group_num_1]
          
city_both_conn_num=['1']*N
ched_city=set()
for ch_city in list(city_road_train):
  if not ch_city in ched_city:
    road_group_num=city_roadgroup_dict[ch_city]
    train_group_num=city_traingroup_dict[ch_city]
    intersect_group=roadgroup_city_dict[road_group_num] & traingroup_city_dict[train_group_num]
    ched_city|=intersect_group
    
    conn_size=str(len(intersect_group))
    for conn_city in list(intersect_group):
      city_both_conn_num[conn_city-1]=conn_size


print(' '.join(city_both_conn_num))