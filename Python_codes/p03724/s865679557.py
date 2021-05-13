N, M = map(int,input().split(' '))
A = []
B = set() #奇数のものだけ入れる
for i in range(M):
    a,b = map(int,input().split(' '))
    A.append([a,b])
    if a in B:
        B.remove(a)
    else:
        B.add(a)
    if b in B:
        B.remove(b)
    else:
        B.add(b)

if len(B) == 0:
    print('YES')
else:
    print('NO')