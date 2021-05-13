import sys

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

if sum(A)<=sum(B):
    print(-1)
    sys.exit()

Y=0
K=0
Q=[]

for i in range(N):
    k=A[i]-B[i]
    if k>0:
        Q.append(k)
    elif k<0:
        K+=1
        Y+=-k

if Y==0:
    print(0)
    sys.exit()
    
Q.sort(reverse=True)
for q in Q:
    Y-=q
    K+=1
    if Y<=0:
        print(K)
        sys.exit()
    
