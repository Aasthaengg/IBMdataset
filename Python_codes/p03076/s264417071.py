dishes_time = []
dishes_time.append(int(input()))
dishes_time.append(int(input()))
dishes_time.append(int(input()))
dishes_time.append(int(input()))
dishes_time.append(int(input()))

temp = 10
index = 0
for i,dish in zip(range(len(dishes_time)),dishes_time):
    if temp > int(str(dish)[-1]) and int(str(dish)[-1])!=0:
        temp = int(str(dish)[-1])
        index = i

for i in range(len(dishes_time)):
    if index != i:
        if dishes_time[i]%10!=0:
            dishes_time[i] = (dishes_time[i]//10)*10 + 10
print(sum(dishes_time))
