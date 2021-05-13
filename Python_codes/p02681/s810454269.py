s=str(input())
t=str(input())
slist=list(s)
tlist=list(t)
del tlist[-1]
if slist==tlist:
    print("Yes")
else :
    print("No")