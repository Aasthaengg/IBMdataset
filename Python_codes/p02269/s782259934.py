n = int(input())
data = {}
for i in range(n):
    a,b = map(str,input().split())
    if a == "insert":
        data[b] = 1
    else:
        if b in data:
            print("yes")
        else:
            print("no")
