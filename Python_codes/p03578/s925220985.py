n=int(input())
d=list(map(int,input().split()))
d.sort()
m=int(input())
t=list(map(int,input().split()))
t.sort()
dd=d.pop()
tt=t.pop()
while d or t:
    if tt==dd:
        if t:
            tt=t.pop()
        else:
            print("YES")
            exit()
        if d:
            dd=d.pop()
        else:
            print("NO")
            exit()
        
    elif tt!=dd:
        if len(d)==0:
            print("NO")
            exit()
        dd=d.pop()
if dd==tt:
    print("YES")
else:
    print("NO")