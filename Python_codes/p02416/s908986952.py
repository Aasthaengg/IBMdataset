list1 = []
while True:
    x = str(input())
    if x == '0':
        break
    else:
        result=0
        for i in x:
            result += int(i)
        list1.append(result)
            
for i in list1:
    print(i)