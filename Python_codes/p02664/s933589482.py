import sys
sys.setrecursionlimit(10**6)
t=input()
tl=list(t)
tln=len(t)
x=0
for x in range(tln):
    if tl[x] == "?":
        if x == tln-1:
            tl[x]="D"
            break
        elif x==0:
            if tl[x+1]=="?":
                tl[x]="P"
                tl[x+1]="D"
            else:
                tl[x]="D"
        elif tl[x-1]=="P":
            tl[x]="D"
        elif tl[x+1]=="?":
            tl[x]="P"
            tl[x+1]="D"
        elif tl[x+1]=="D":
            tl[x]="P"
        else:
            tl[x]="D"
t="".join(tl)
print(t)