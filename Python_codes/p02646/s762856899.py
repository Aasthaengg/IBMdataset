a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
l=abs(a-b)
if l==0:
    print('YES')
else:
    if w>=v:
        print('NO')
    else:
        if l<=t*(v-w):
            print('YES')
        else:
            print('NO')