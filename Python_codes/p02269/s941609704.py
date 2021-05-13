num = int(input())
sets = set()
for n in range(num):
    temp = input()
    if temp[0] == 'i':
        sets.add(temp.split(' ')[1])
    else:
        if temp.split(' ')[1] in sets:
            print("yes")
        else:
            print("no")