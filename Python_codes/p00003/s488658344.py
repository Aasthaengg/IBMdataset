
round = int(input(""))
for i in range (0,round):
    arr = []
    temp = input("")
    a,b,c = temp.split(" ")
    arr.append(int(a))
    arr.append(int(b))
    arr.append(int(c))
    arr.sort()
    if(pow(arr[0],2)+pow(arr[1],2)==pow(arr[2],2)):
        print("YES")
    else:
        print("NO")

