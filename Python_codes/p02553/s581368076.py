list=input().split(" ")

list1=[list[0], list[1]]
list2=[list[2], list[3]]

list_a=[int(x)*int(y) for x in list1 for y in list2]

print(max(list_a))