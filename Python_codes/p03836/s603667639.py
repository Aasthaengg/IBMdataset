p,q,x,y=map(int,input().split())
x-=p
y-=q
print('U'*y+'R'*x+'D'*y+'L'*x+'L'+'U'*-~y+'R'*-~x+'D'+'R'+'D'*-~y+'L'*-~x+'U')