n=int(input())
A=list(map(int,input().split()))

if n==2:
    print(abs(A[0]-A[1]))
    print(*A)
    exit()
A.sort()
menos=[] ; plus=[]
for i in range(len(A)):
    if A[i]<0:
        menos.append(A[i])
    else:
        plus.append(A[i])
if menos==[]:
    print(sum(plus)-plus[0]*2)
    res=plus[0]
    for i in range(n-2):
        print(res, A[i+1])
        res=res-A[i+1]
    print(A[n-1], res);exit()
        
elif plus==[]:
    print(-sum(menos)+ menos[-1]*2)
    res=menos[-1]
    for i in range(n-1):
        print(res,menos[i])
        res=res-menos[i]
    exit()
    

print(sum(plus)-sum(menos))
m=len(menos); p=len(plus)
if p==1:
    res=plus[-1]
    for i in range(n-1):
        print(res,menos[i])
        res=res-menos[i]
    exit()
if m==1:
    res=menos[0]
    for i in range(n-2):
        print(res, plus[i])
        res=res-plus[i]
    print(plus[-1], res);exit()

Q= plus[1:]+ [menos[0]]
W= menos[1:]+[plus[0]] ;#print(Q,W)

res=W[-1]
for i in range(len(W)-1):
    print(res,W[i])
    res=res-W[i]
rec=Q[-1]
for i in range(len(Q)-1):
    print(rec, Q[i])
    rec=rec-Q[i]
print(res,rec)