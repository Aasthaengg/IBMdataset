n = int(input())

time_list = list(map(int,input().split()))

m = int(input())

drink_num_time = []
drink_time = []

for i in range(m):
    drink_num_time.append(list(map(int,input().split())))

normal_time = sum(time_list)


for i in range(m):
    drink_time.append(normal_time+drink_num_time[i][1]-time_list[(drink_num_time[i][0])-1])

for i in range(m):
    print(drink_time[i])
