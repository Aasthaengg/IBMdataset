a,b = map(int, input().split())
ans = [['.' for i in range(50)]+['#' for i in range(50)]for j in range(100)]

x,y = 0,51
while a>1:
    ans[x][y] = '.'
    y+=2
    if y>99:
        x+=2
        y=51
    a-=1

x,y = 0,0
while b>1:
    ans[x][y] = '#'
    y+=2
    if y>48:
        x+=2
        y=0
    b-=1

print(100,100)

for i in range(100):
    print(''.join(ans[i]))
