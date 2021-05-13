X,Y=map(int,input().split())
X=4 if X>3 else X
Y=4 if Y>3 else Y

C=[300000,200000,100000,0]

print(C[X-1]+C[Y-1]+400000 if X==Y==1 else C[X-1]+C[Y-1])