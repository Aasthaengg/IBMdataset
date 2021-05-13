x,y = map(int, input().split())

al = [1,3,5,7,8,10,12]
bl = [4,6,9,11]
cl = [2]

if x in al:
    if y in al:
        print("Yes")
    else:
        print("No")
        
elif x in bl:
    if y in bl:
        print("Yes")
    else:
        print("No")
else:
    print("No")