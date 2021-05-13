x, y, z = map(int,input().split())
a =[x]
b =[y]
c =[z]
if a[0] == b[0] == c[0]:
    if a[0] % 2 == 1:
        print(0)
        exit()
        
    else:
        print('-1')
        exit()
        
for i in range(1000):
    if a[i] % 2 == 0 and b[i] % 2 == 0 and c[i] % 2 == 0:
        a.append((b[i] + c[i]) // 2)
        b.append((a[i] + c[i]) // 2)
        c.append((b[i] + a[i]) // 2)
    
    else:
        print(i)
        exit()