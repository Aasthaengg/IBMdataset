#n=int(input())
x,y=map(str,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
l=list('ABCDEF')
xind=l.index(x)
yind=l.index(y)
if xind < yind :
    print('<')
elif xind > yind :
    print('>')
else:
    print('=')

