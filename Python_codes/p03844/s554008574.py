x = input().split()
a = int(x[0])
c = int(x[2])
if x[1] == '+':
    print(a + c)
elif x[1] == '-':
    print(a - c)
else:
    print('error')