num = input()
num_1 = num.split()
a = int(num_1[0])
b = int(num_1[1])
c = int(num_1[2])
count = 0
while a <= b:
    if c % a == 0:
        count += 1
    a += 1

print(count)