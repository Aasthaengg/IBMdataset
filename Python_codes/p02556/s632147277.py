n = int(input())
hidarisita=2*10**9
migiue=0
migisita=2*10**9
hidariue=-10**9
x=[]
for i in range(0,n):
    x.append(list(map(int, input().split())))
    
for i in range(0,n):#左下
    minlocal=x[i][0]+x[i][1]
    if minlocal<hidarisita:
        hidarisita=minlocal
    if minlocal==hidarisita:
        hidarisita2=minlocal
for i in range(0,n):#右上
    maxlocal=x[i][0]+x[i][1]
    if maxlocal>migiue:
        migiue=maxlocal
    if maxlocal==migiue:
        migiue2=maxlocal
for i in range(0,n):#右下
    minlocal=-x[i][0]+x[i][1]
    if minlocal<migisita:
        migisita=minlocal
    if minlocal==migisita:
        migisita2=minlocal
for i in range(0,n):#左上
    maxlocal=-x[i][0]+x[i][1]
    if maxlocal>hidariue:
        hidariue=maxlocal
    if maxlocal==hidariue:
        hidariue2=maxlocal
aa=migiue-hidarisita
ab=migiue-hidarisita2
ba=migiue2-hidarisita
bb=migiue2-hidarisita2
cc=hidariue-migisita
cd=hidariue-migisita2
dc=hidariue2-migisita
dd=hidariue2-migisita2
print(max(aa,ab,ba,bb,cc,cd,dc,dd))