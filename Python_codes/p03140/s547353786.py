n = int(input())
a = str(input())
b = str(input())
c = str(input())

p = 0
for i in range(n):
    t = 0
    if(a[i] != b[i]):
        t += 1
    if(b[i] != c[i]):
        t += 1
    if(a[i] != c[i]):
        t += 1

    if(t == 3):
        p += 2
    elif(t == 0):
        pass
    else:
        p += 1
print(p)