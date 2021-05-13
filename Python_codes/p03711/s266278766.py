a,b = map(int,input().split())
list1 = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]
list3 = [2]

if list1.count(a) == 1:
    if list1.count(b) == 1:
        print("Yes")
    else:
        print("No")
if list2.count(a) == 1:
    if list2.count(b) == 1:
        print("Yes")
    else:
        print("No")
if list3.count(a) == 1:
    if list3.count(b) == 1:
        print("Yes")
    else:
        print("No")