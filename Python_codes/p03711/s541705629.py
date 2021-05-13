x,y =map(int,input().split())
a = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
flag = False
for i in a:
    if x in i:
        if y in i:
            flag =True
            break
print('Yes' if flag else 'No')