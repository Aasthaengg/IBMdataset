a,b = map(int,input().split())
c,d = (a-1)//50, (a-1)%50
e,f = (b-1)//50, (b-1)%50

print(100,100)
res = [['#']*100 for _ in range(50)] + [['.']*100 for _ in range(50)]

# white
for i in range(c):
    for j in range(0,100,2):
        res[i*2][j] = '.'
for i in range(d):
    res[c*2][c%2+i*2] = '.'
# black
for i in range(e):
    for j in range(0,100,2):
        res[99-i*2][j] = '#'
for i in range(f):
    res[99-e*2][e%2+i*2] = '#'

for i in range(100):
    print(''.join(res[i]));
