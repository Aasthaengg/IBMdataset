data =  input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])

x = b + min(c,a+b+1)

print(x)