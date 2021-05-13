P = [1 for _ in range(10**5)]
P[0]=0
P[1]=0
for i in range(2,int((10**5)**0.5)+1):
    for j in range(i*i,10**5,i):
        P[j]=0
Q = []
for i in range(3,10**5,2):
    if P[i]==1 and P[(i+1)//2]==1:
        Q.append(i)
A = [0 for _ in range(10**5+1)]
for q in Q:
    A[q] = 1
for i in range(1,10**5+1):
    A[i] += A[i-1]
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    print(A[r]-A[l-1])