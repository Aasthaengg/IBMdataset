r, D, x = map(int, input().split())

def num(i):
    return r*i-D

a = x
for i in range(10):
    a = num(a)
    print(a)
    
