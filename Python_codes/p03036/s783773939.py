r, d, x0 = map(int,input().split())

def mo(i):
    if i == 0:
        return x0
    return r*mo(i-1) - d 

for i in range(1,11):
    print(mo(i))
