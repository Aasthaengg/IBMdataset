a = input()
b = a.split(' ')
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
b.sort()
print(str(b[0])+' '+str(b[1])+' '+str(b[2]))