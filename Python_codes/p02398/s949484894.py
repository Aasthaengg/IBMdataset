count = 0
x = raw_input()
x = x.split(" ")
a = int(x[0])
b = int(x[1])
c = int(x[2])
for num in range(a,b+1):
    tmp = c%num
    if(tmp == 0):
        count += 1
print(count)
