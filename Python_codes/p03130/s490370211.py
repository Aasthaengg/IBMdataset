a = []
for i in range(3):
    x,y = map(int,input().split())
    a.append(x)
    a.append(y)

odd = 0
for i in range(1,5):
    x = a.count(i)
    if x % 2 == 1:
        odd += 1
if odd <= 2:
    print('YES')
else:
    print('NO')