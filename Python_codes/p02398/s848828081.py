x = input()
y = x.split(' ')
a = int(y[0])
b = int(y[1])
c = int(y[2])
count = a
count2 = 0
while count<=b:
    if c % count == 0:
        count2 += 1
    count += 1
else:
    print(count2)