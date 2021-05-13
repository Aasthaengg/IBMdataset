N=int(input())
data=[input().split() for i in range(N)]
data_name=[]
for i in range(N):
    if data[i][0] in data_name:
        continue
    else:
        data_name.append(data[i][0])
data_name_sort=sorted(data_name)
#print(data_name_sort)
data_point=[]
for i in range(N):
    num=0
    for j in range(len(data_name_sort)):
        if data[i][0]==data_name_sort[j]:
            num+=(len(data_name)-j)*200+int(data[i][1])
        else:
            continue
    data_point.append(num)
#print(data_point)
data_sort=[i for i, _ in sorted(enumerate(data_point), key=lambda x:x[1])][::-1]
#print(data_sort)
for i in range(N):
    ans=int(data_sort[i])+1
    print(ans)