S = input()
for i in range(9):
    hikaku = str(i)+str(i)+str(i)
    #print(hikaku)
    if (hikaku in S) == True:
        result = "Yes"
        break
    else:
        result = "No"
print(result)