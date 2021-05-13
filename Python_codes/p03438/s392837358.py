n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
aa=sum(A) ; bb=sum(B)
if aa>bb:
    print("No");exit()
if aa==bb:
    if A==B:print("Yes");exit()
    print("No");exit()

C=[i-j for i,j in zip(A,B)]
D=[[0,0]]*n
for i in range(n):
    if C[i]>=0:
        D[i]= [0,C[i]]
    else:
        D[i]= [(-C[i]+ (C[i]%2))//2 , C[i]%2]
if sum([i[0] for i in D])>= sum([l[1] for l in D]):
    print("Yes")
else:
    print("No")