SX,SY,TX,TY=map(int,input().split())
x=TX-SX
y=TY-SY
print(''.join(['U'*y,'R'*x,'D'*y,'L'*x,'L','U'*(y+1),'R'*(x+1),'D','R','D'*(y+1),'L'*(x+1),'U']))