a,b,c,d=map(int,input().split())
x=c-a
y=d-b
print('U'*y+'R'*x+'D'*y+'L'*-~x+'U'*-~y+'R'*-~x+'DR'+'D'*-~y+'L'*-~x+'U')
