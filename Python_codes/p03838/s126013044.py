x,y=map(int,input().split())
#print(y-x,x-y+2,1+y+x,(-y-x)+1,y+x+1)

l=[]
if y-x>=0:
    l.append(y-x)
if x-y+2>=0:
    l.append(x-y+2)
if 1+y+x>=0:
    l.append(1+y+x)
if (-y-x)+1>=0:
    l.append((-y-x)+1)
if y+x+1>=0:
    l.append(y+x+1)
print(min(l))

'''
add=max(abs(x),abs(y))-min(abs(x),abs(y))
cnt=add
if x*y<0:
    cnt=cnt+1
elif ((abs(x)>abs(y))and(x>0)and(y>0))or((abs(x)<abs(y))and(x<0)and(y<0)):
    cnt=cnt+2
else:
    cnt=cnt
if y==0:
    cnt=cnt-1
print(cnt)
'''
