import sys
list = sys.stdin.readlines()

e=0
GCD = 0
def Euclide(a, b):
    if b == 0:
        return a
    if a < b:
        tmp = a
        a = b
        b = tmp
    e = a%b
    return Euclide(b, e)

for i in list:
    i = i.split(' ')
    GCD = Euclide(int(i[0]), int(i[1]))
    print(str(GCD)+" "+str(int(int(i[0])/GCD*int(i[1]))))