n = int(input())
temochi=[]
for i in range(n):
    temochi.append(input())
for x in ['S','H','C','D']:
    for y in range(1,14):
        z = '{} {}'.format(x,y)
        if not(z in temochi): print(z)