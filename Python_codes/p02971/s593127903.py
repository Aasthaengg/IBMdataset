import copy
n = int(input())
lst =[]
for i in range(n):
    x = int(input())
    lst.append(x)

lst2 = copy.deepcopy(lst)
lst2.sort()
max = max(lst2)
for x in lst:
    if x == max:
        print(lst2[-2])
    else:
        print(max)