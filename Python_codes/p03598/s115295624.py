import math
def py():
    print("Yes")
def pn():
    print("No")
def iin():
    x = int(input())
    return x

neko = 0
nya = 0
nuko = 0
n = iin()
k = iin()
x = [int(x) for x in input().split()]

for i in range(n):
    if(abs(x[i]-k) < x[i]):
        neko = neko + 2*abs(x[i]-k)
    else:
        neko = neko + 2*x[i]
print(neko)