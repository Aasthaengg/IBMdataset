from collections import Counter,OrderedDict

N=int(input())
a=list(map(int,input().split()))
d=OrderedDict(Counter(a))
e=list(d)
e.sort()

if len(d)>3:
    ans="No"
else:
    ans="No"
    if len(d)==1:
        if e[0]==0:
            ans="Yes"
    elif len(d)==2:
        if N%3==0:
            if e[0]==0 and d[0]==N//3 and d[e[1]]==2*N//3:
                ans="Yes"
    else:
        if N%3==0:
            if d[e[0]]==d[e[1]]==d[e[2]]:
                if e[0]^e[1]^e[2]==0:
                    ans="Yes"
                   
print(ans)
