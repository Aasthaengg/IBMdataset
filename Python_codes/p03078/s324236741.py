X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

def condition(num):
    count=0
    for i in range(0,Z):
        subcount=0
        a=num-C[i]
        s=0
        t=Y-1
        while X-1>=s and t>=0:
            if A[s]+B[t]>=a:
                t-=1
            else:
                subcount+=t+1
                s+=1
        count+=X*Y-subcount
    return count>=K

start=0
end=10**12
while end-start>1:
    test=(end+start)//2
    if condition(test):
        start=test
    else:
        end=test

Kth=0
if condition(end):
    Kth=end
else:
    Kth=start

ans=[]
for i in range(0,Z):
    a=Kth+1-C[i]
    s=0
    t=Y-1
    while X-1>=s and t>=0:
        if A[s]+B[t]>=a:
            for j in range(s,X):
                ans.append(A[j]+B[t]+C[i])
            t-=1
        else:
            s+=1

for i in range(0,K-len(ans)):
    ans.append(Kth)
ans.sort()
for i in range(0,K):
    print(ans[-i-1])
