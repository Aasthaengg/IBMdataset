import copy
N=int(input())
A=list(map(int,input().split()))
allcost=abs(0-A[0])
for i in range(N-1):
    allcost=allcost+abs(A[i]-A[i+1])
allcost=allcost+abs(A[N-1])
#print(allcost)
A.insert(0,0)
A.append(0)
for i in range(N):
    print(allcost-abs(A[i+1]-A[i])-abs(A[i+2]-A[i+1])+abs(A[i+2]-A[i]))
