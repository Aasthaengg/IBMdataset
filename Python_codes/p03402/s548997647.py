a,b = map(int,input().split())
a,b = a-1, b-1

w,x = a//50, a%50
y,z = b//50, b%50

print(100,100)
res = [['#' for _ in range(100)] for i in range(50)]
res += [['.' for _ in range(100)] for i in range(50)]

for i in range(0,w*2,2):
    for j in range(0,100,2):
        res[i][j] = '.'
for j in range(0,x*2,2):
    res[2*w][j] = '.'

for i in range(99,99-y*2,-2):
    for j in range(0,100,2):
        res[i][j] = '#'
for j in range(0,z*2,2):
    res[99-y*2][j] = '#'

for l in res:
    print(''.join(l))
