dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

x, y = input().split()

if(dic[x] > dic[y]):
    print(">")
elif(dic[x] < dic[y]):
    print("<")
else:
    print("=")