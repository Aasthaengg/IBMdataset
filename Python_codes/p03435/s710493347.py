L= [list(map(int, input().split())) for i in range(3)]
s=True

if L[1][1]!=L[1][0]-L[0][0]+L[0][1]:
    s=False
if L[1][2]!=L[1][0]-L[0][0]+L[0][2]:
    s=False
if L[2][1]!=L[2][0]-L[0][0]+L[0][1]:
    s=False
if L[2][2]!=L[2][0]-L[0][0]+L[0][2]:
    s=False
if s:
    print('Yes')
else:
    print('No')