N=int(input())
A=[[0]]
for i in range(N):
    a=list(map(int,input().split()))
    a+=[0]
    A.append(a)
    
#print(A)
B=[0 for i in range(N+1)]
C=[a for a in range(1,N+1)]
cnt=0
for i in range(10**6):
    D=[]
    F=0
    for j in C:
        if A[A[j][B[j]]][B[A[j][B[j]]]]==j and j not in D and A[j][B[j]] not in D:
            D.append(j)
            D.append(A[j][B[j]])
            B[A[j][B[j]]]+=1
            B[j]+=1
            F=1
            cnt+=1
            #print("A",i,B,D)
            #print(A[j][B[j]],B,D)
    if F==0:
        break
    D.sort()
    C=D
    
if cnt==N*(N-1)//2:
    print(i)
else:
    print(-1)