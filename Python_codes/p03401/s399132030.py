from collections import deque
N=int(input())
A=list(map(int,input().split()))
A.insert(0,0)
A.extend([0])
s=0
for i in range(1,N+2):
    s+=abs(A[i]-A[i-1])
for i in range(1,N+1):
    print(s-((abs(A[i-1]-A[i])+abs(A[i]-A[i+1]))-abs(A[i-1]-A[i+1])))