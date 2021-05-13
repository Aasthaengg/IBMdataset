import sys
input=sys.stdin.readline
A,B,M=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(M):
    xi,yi,ci=list(map(int,input().split()))
    c.append(a[xi-1]+b[yi-1]-ci)
a.sort()
b.sort()
c.sort()
print(min(a[0]+b[0],c[0]))