h,w,k=map(int,input().split())
c=[list(input())for i in range(h)]
d=0
for i in range(2**h):
    for j in range(2**w):
        x=bin(i)[2:]
        y=bin(j)[2:]
        x="0"*(h-len(x))+x
        y="0"*(w-len(y))+y
        p=0
        for s in range(h):
            for t in range(w):
                if x[s]==y[t]=="0" and c[s][t]=="#":
                    p+=1
        if p==k:
           d+=1
print(d)