import heapq

N,M=map(int,input().split())
A=list(map(int,input().split()))

D={}
for _ in range(M):
    B,C=map(int,input().split())
    if -C in D:
        D[-C]+=B
    else:
        D[-C]=B

H=list(D.items())
heapq.heapify(H)

G=[]
Y=0
while Y<N and H:
    (a,k)=heapq.heappop(H)
    a=-a
    k=min(k,N-Y)
    A+=[a]*k
    Y+=k

A.sort(reverse=True)
print(sum(A[:N]))