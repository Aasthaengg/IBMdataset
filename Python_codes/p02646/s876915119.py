import sys
a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if v<=w:
    print('NO')
    sys.exit()
else:
    d=abs(a-b)
    s=v-w
    if d<=t*s:
        print('YES')
        sys.exit()
print('NO')