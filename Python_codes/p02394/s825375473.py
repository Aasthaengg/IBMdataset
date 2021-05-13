n = input().split()
W = int(n[0])
H = int(n[1])
x = int(n[2])
y = int(n[3])
r = int(n[4])

if x+r > W:
    print('No')
else:
    if y+r > H:
        print('No')
    elif x < 0 or y < 0:
        print('No')
    else:
        print('Yes')