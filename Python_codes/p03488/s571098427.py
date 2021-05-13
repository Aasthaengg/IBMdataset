s=input().split('T')
x,y=map(int,input().split())
dx,dy={0},{0}
for i,a in enumerate(map(len,s[::2])):
    if i:dx=set(t+a for t in dx)|set(t-a for t in dx)
    else:dx={a}
for b in map(len,s[1::2]):dy=set(t+b for t in dy)|set(t-b for t in dy)
if x in dx and y in dy:print('Yes')
else:print('No')