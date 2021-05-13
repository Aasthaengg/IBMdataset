a = int(input())

def f1(i):
    lst = []
    while i > 0:
        lst.append(i%10)
        i //= 10
    lst.reverse()
    return lst

b = f1(a)
c = 0
for i in range(4):
    if b[i]==2:
        c += 1
    else:
        c = c

print(c)
    
