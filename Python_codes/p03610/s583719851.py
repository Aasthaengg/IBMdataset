din = str(input())
dout = ""
length = len(din)
for i in range(int(length/2)+int(length%2)):
    dout = dout + din[2*i]
print(dout)