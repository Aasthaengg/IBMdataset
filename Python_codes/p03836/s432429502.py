sx,sy,tx,ty = map(int,input().split())
no1 = ''
for i in range(ty-sy):
    no1 += 'U'
for i in range(tx-sx):
    no1 += 'R'
no2 = ''
for i in range(ty-sy):
    no2 += 'D'
for i in range(tx-sx):
    no2 += 'L'
print(no1+no2+'LU'+no1+'RD'+'RD'+no2+'LU')
