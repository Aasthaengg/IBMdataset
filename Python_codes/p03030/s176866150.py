n = int(input())

S=[]
for i in range(n):
    c,p = map(str,input().split())
    S.append( [c,int(p)] )

C=[0]*n
for i in range(n):
    for j in range(n):
        if S[i][0]>S[j][0]:
            C[i]+=1
        elif S[i][0]==S[j][0]:
            if S[i][1]<S[j][1]:
                C[i]+=1

A=[0]*n
for i in range(n):
    print( C.index(i)+1 )

