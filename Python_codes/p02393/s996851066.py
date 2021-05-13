abc = input()
list_abc = abc.split(" ")
min = int(list_abc[0])
mid = int(list_abc[1])
max = int(list_abc[2])

for index in range(3):
    cur_num = int(list_abc[index])
    if max < cur_num:
        list_abc[2] = str(cur_num)
        list_abc[index] = str(max)
        max = cur_num
min = int(list_abc[0])
mid = int(list_abc[1])
if mid < min :
    list_abc[0] = str(mid)
    list_abc[1] = str(min)
min = int(list_abc[0])
mid = int(list_abc[1])
print(str(min) + " " + str(mid) + " " + str(max))
max = int(list_abc[2])
