a = int(input())
b = []
for i in range(1,a+1):
    if i%3 == 0:
        b.append(i)
    elif i%10 == 3:
        b.append(i)
    elif (i//10)%10 == 3:
        b.append(i)
    elif((i//10)//10)%10 == 3:
        b.append(i)
    elif((i//10)//10)//10%10 == 3:
        b.append(i)
    elif((i//10)//10)//10//10%10 == 3:
        b.append(i)
    elif((i//10)//10)//10//10//10%10 == 3:
        b.append(i)
    else:
        continue
for i in b:
    print(" "+str(i),end="")
print("\n",end="")
