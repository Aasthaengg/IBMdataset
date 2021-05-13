S = input()
for i in range(9):
    hikaku = str(i)+str(i)
    #print(hikaku)
    if (hikaku in S) == True:
        result = "Bad"
        break
    else:
        result = "Good"
print(result)