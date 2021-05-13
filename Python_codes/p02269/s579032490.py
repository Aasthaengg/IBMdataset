n = int(input())
myDict = {}

for i in range(n):
    cmd,key = input().split()
    if cmd == "insert":
        myDict.setdefault(key,key)
    else:
        if key in myDict.keys():
            print("yes")
        else:
            print("no")
