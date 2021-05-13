a,b = map(int,input().split())
if (a != 0) and (b != 0):
    print(str(int(a*(a-1)/2 + b*(b-1)/2)))
elif (a == 0) and (b == 0):
    print("0")      
elif (a == 0) and (b != 0):
    print(str(int(b*(b-1)/2)))
else:
    print(str(int(a*(a-1)/2)))