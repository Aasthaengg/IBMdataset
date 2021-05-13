n=int(input())
c=list(input())
numW=0
numR=c.count("R")
W=n-numR
a=[]
if numR==0 or W==0:
    print(0)
else:
    for i in range(n):
        if c[i]=="W":
            numW+=1
        else:
            numR-=1
        a.append(max(numR,numW))
    print(min(a))