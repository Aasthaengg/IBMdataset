X,Y=map(int,input().split())
number=0
for i in range(X+1):
    if 2*i + 4*(X-i) == Y:
        number += 1
    else:
        number += 0
if number > 0:
    print('Yes')
else:
    print('No')

