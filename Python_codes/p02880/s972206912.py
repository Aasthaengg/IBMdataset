user_input= int(input())
found= False
for counter in range(1, 10):
    for index in range(1, 10):
        if (counter * index)==user_input:
            found= True
            break
if found==True:
    print("Yes")
else:
    print("No")