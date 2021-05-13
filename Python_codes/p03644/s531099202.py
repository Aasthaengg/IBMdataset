n = int(input())

maxdivisiontimes = -1
while n != 0:
    flag = True
    checkcounter = 0
    checkno = n
    while flag == True:
        if checkno % 2 == 0:
            checkcounter += 1
        checkno = checkno // 2 
        if checkno == 1 or checkno == 0:
            flag = False
    if maxdivisiontimes < checkcounter:
        maxdivisiontimes = checkcounter
        maxdivisionno = n
    n -= 1
print(maxdivisionno)