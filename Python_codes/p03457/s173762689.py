import sys
readline=sys.stdin.readline
read=sys.stdin.read
n,*abc=map(int,read().split())

abc=[(t,x,y) for t,x,y in zip(*[iter(abc)]*3)]
abc=[(0,0,0)]+abc
diff=[abs(nxt[2]-cur[2])+abs(nxt[1]-cur[1])-nxt[0]+cur[0] for cur,nxt in zip(abc,abc[1:])]
for d in diff:
  if d>0 or d%2==1:
    print('No')
    break
else:
  print('Yes')