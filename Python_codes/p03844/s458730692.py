value = str(input())
data = value.split()
if(data[1] == "+"):
    m = int(data[0]) + int(data[2])
elif(data[1] == "-"):
    m = int(data[0]) - int(data[2])
print(m)

