o1,o2,x,y=map(int,input().split())
x = x-o1
y = y-o2
res = ''
if x>=0 and y>=0:
    res='R'*x+'U'*y+'L'*x+'D'*y
    res+='L'+'U'*(y+1)+'R'*(x+1)+'D'
    res+='R'+'D'*(y+1)+'L'*(x+1)+'U'
print(res)