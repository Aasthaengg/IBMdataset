str = input()
p = input()

for i in range(len(str)):
    strtemp = str[i:len(str)] + str[0:i]
    if p in strtemp:
        print("Yes")
        break
else:
    print("No")
