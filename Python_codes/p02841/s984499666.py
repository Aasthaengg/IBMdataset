l=[31,28,31,30,31,30,31,31,30,31,30,31]
s=list(map(int,input().split()))
d=list(map(int,input().split()))
x=l[s[0]-1]
if(x!=s[1]):
    print(0)
else:
    print(1)
