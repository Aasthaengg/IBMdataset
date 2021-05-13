list=[]
for i in input().split():
    if i=='+':
        list[len(list)-2]=int(list[len(list)-2])+int(list[len(list)-1])
        list.pop()
    elif i=='-':
        list[len(list)-2]=int(list[len(list)-2])-int(list[len(list)-1])
        list.pop()
    elif i=='*':
        list[len(list)-2]=int(list[len(list)-2])*int(list[len(list)-1])
        list.pop()
    else:
        list.append(i)
print(list[0])


