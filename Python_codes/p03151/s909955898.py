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

Q.sort()

while Y>0:
    q=Q.pop()
    Y-=q
    K+=1

print(K)    
