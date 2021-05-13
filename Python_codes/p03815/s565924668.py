x=int(input())
if(x<=6):
    print(1)
elif(x<=11):
    print(2)
elif(x>11 and x%11==0):
    print((x//11)*2)
elif(x>11 and x%11<=6):
    print((x//11)*2+1)
elif(x>11 and x%11>6):
    print((x//11)*2+2)