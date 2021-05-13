p,q,x,y=map(int,input().split())
x-=p
y-=q
u='U'*y+'R'*x
d='D'*y+'L'*x+'LU'
print(u+d+u+'RDRD'+d)