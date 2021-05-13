abc = input()
num_abc = abc.split()
a = int(num_abc[0])
b = int(num_abc[1])
c = int(num_abc[2])
if a < b < c:
    print('Yes')
else:
    print('No')