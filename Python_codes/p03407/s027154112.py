money = input()
lis = money.split()
if int(lis[0]) + int(lis[1]) >= int(lis[2]):
    print("Yes") 
else:
    print("No")