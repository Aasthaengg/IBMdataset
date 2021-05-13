a, b = input().split()
a = int(a)
b = int(100*int(b[0])+10*int(b[2])+int(b[3]))
#print(b)
c = a*b // 100
c = int(c)
print(c)