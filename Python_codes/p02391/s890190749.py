a = input()
b =a.split()
if(int(b[0]) == int(b[1])):
    print('a == b')
elif(int(b[0]) < int(b[1])):
    print('a < b')
else:
    print('a > b')