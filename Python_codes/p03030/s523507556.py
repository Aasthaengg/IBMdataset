n = int(input())
list = []
for xi in range(n):
    add1, add2 = input().split()
    add = [int(add2), add1, xi+1]
    list.append(add)
list.sort(key=lambda list2: list2[1])


name = list[0][1]
list2 = [list[0]]
count = 1
for xi in range(1,n):
    if name == list[xi][1]:
        list2.append(list[xi])
        count += 1
    else:
        list2.sort()
        for yi in range(count-1,-1,-1):
            print(list2[yi][2])
        name = list[xi][1]
        list2 = [list[xi]]
        count = 1

if len(list2)<n:
    list2.sort()
for yi in range(count-1,-1,-1):
    print(list2[yi][2])
name = list[xi][1]
list2 = [list[xi]]
count = 1
