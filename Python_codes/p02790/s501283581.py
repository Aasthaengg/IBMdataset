list1=input().split()
A=(list1[0])*(int(list1[1]))
B=(list1[1])*(int(list1[0]))
list2=[A,B]
list2.sort()
print(list2[0])