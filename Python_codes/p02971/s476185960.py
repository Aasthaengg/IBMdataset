n = int(input())
max_1 = 0
max_2 = 0
a_list = []
for i in range(n):
    a = int(input())
    a_list.append(a)
    if max_1 < a:
        max_2 = max_1
        max_1 = a
    elif max_2 < a:
        max_2 = a
#print(max_1,max_2)
for i in range(n):
    if a_list[i] == max_1:
        print(max_2)
    else:
        print(max_1)
