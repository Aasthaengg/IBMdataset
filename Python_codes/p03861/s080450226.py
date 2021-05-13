a,b,x=map(int,input().split())

if a==0:
    fl=-1
else:
    fl=(a-1)//x

cl=b//x

print(cl-fl)