lst = list(input())
for i,num in enumerate(lst):
    lst[i] = int(num)

if lst[0]+lst[1]+lst[2]+lst[3]==7:
    print(str(lst[0])+"+"+str(lst[1])+"+"+str(lst[2])+"+"+str(lst[3])+"=7")
elif lst[0]+lst[1]+lst[2]-lst[3]==7:
    print(str(lst[0])+"+"+str(lst[1])+"+"+str(lst[2])+"-"+str(lst[3])+"=7")
elif lst[0]+lst[1]-lst[2]+lst[3]==7:
    print(str(lst[0])+"+"+str(lst[1])+"-"+str(lst[2])+"+"+str(lst[3])+"=7")
elif lst[0]+lst[1]-lst[2]-lst[3]==7:
    print(str(lst[0])+"+"+str(lst[1])+"-"+str(lst[2])+"-"+str(lst[3])+"=7")
elif lst[0]-lst[1]+lst[2]+lst[3]==7:
    print(str(lst[0])+"-"+str(lst[1])+"+"+str(lst[2])+"+"+str(lst[3])+"=7")
elif lst[0]-lst[1]+lst[2]-lst[3]==7:
    print(str(lst[0])+"-"+str(lst[1])+"+"+str(lst[2])+"-"+str(lst[3])+"=7")
elif lst[0]-lst[1]-lst[2]+lst[3]==7:
    print(str(lst[0])+"-"+str(lst[1])+"-"+str(lst[2])+"+"+str(lst[3])+"=7")
elif lst[0]-lst[1]-lst[2]-lst[3]==7:
    print(str(lst[0])+"-"+str(lst[1])+"-"+str(lst[2])+"-"+str(lst[3])+"=7")