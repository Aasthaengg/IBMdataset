s = input()
n = int(s)
if(n < 1000):
    print(1000 - n)
elif(s[-3:] == "000"):
    print(0)
else:
    print(1000 - int(s[-3:]))