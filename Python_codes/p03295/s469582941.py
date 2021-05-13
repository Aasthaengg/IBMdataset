import sys
#print(316736)
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from operator import itemgetter
N,M=map(int,readline().split())
ab=[]
#print(112)
for i in range(M):
    x,y=map(int,readline().split())
    ab.append((x,y))
#print(111)
ab=sorted(ab,key=itemgetter(1))
ans=0
x=0
for a,b in ab:
    #print(a,x,b)
    if a<=x:
        continue
    x=b-1
    ans+=1
print(ans)