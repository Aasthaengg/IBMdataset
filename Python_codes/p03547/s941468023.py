N16 = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,}
X,Y = input().split()
if N16[X] == N16[Y]:
    print('=')
elif N16[X] > N16[Y]:
    print('>')
else:
    print('<')