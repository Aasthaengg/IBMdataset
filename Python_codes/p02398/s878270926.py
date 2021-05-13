input_line = raw_input().split()
a = int(input_line[0])
b = int(input_line[1])
c = int(input_line[2])
count = 0
for i in range(a,b+1):
    if c%i == 0:
        count += 1
print count