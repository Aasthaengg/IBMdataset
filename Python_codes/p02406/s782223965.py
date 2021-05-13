n = int(input())
l = []
if 0 <= n <= 10000:
    for i in range(1,(n + 1)):
        if i % 3 == 0:
            l.append(str(i))
        elif i % 10 == 3:
            l.append(str(i))
        elif '3' in str(i):
            l.append(str(i))    

print(' ' + ' '.join(l))