N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
A.append(0)
cost = []
for i in range(len(A)-1):
    cost.append(abs(A[i]-A[i+1]))
a = sum(cost)
for i in range(1,N+1):
    print(a-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))