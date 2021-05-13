c = [list(map(int, input().split())) for _ in range(3)]

x1 = c[0][0]-c[1][0]
x2 = c[0][1]-c[1][1] 
x3 = c[0][2]-c[1][2]

x4 = c[1][0]-c[2][0]
x5 = c[1][1]-c[2][1]
x6 = c[1][2]-c[2][2]

if x1==x2 and x2==x3:
    pass
else:
    print('No')
    exit()
if x4==x5 and x5==x6:
    pass 
else:
    print('No')
    exit()

x1 = c[0][0]-c[0][1]
x2 = c[1][0]-c[1][1] 
x3 = c[2][0]-c[2][1]

x4 = c[0][1]-c[0][2]
x5 = c[1][1]-c[1][2]
x6 = c[2][1]-c[2][2]

if x1==x2 and x2==x3:
    pass
else:
    print('No')
    exit()
if x4==x5 and x5==x6:
    pass 
else:
    print('No')
    exit()
print('Yes')