a,b,c,d=map(int,input().split())

x=c-a
y=d-b

t=''
t+='R'*x
t+='U'*y
t+='L'*x
t+='D'*y
t+='D'
t+='R'*(x+1)
t+='U'*(y+1)
t+='L'
t+='U'
t+='L'*(x+1)
t+='D'*(y+1)
t+='R'

print(t)