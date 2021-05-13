num = int(input())
sets = {}
for n in range(num):
    temp = input()
    if temp[0] == 'i':
        sets[temp.split(' ')[1]] = 0
    else:
        if temp.split(' ')[1] in sets:
            print("yes")
        else:
            print("no")