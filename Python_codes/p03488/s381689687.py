t,*s=input().split('T')
x,y=map(int,input().split())
dx,dy={len(t)},{0}
for a in map(len,s[1::2]):dx=set(t+a for t in dx)|set(t-a for t in dx)
for b in map(len,s[::2]):dy=set(t+b for t in dy)|set(t-b for t in dy)
if x in dx and y in dy:print('Yes')
else:print('No')