c=[]
for i in range(3):
    a,b=map(int,input().split())
    c.append(a)
    c.append(b)
if c.count(1)<3 and c.count(2)<3 and c.count(3)<3 and c.count(4)<3:
    print('YES')
else:
    print('NO')