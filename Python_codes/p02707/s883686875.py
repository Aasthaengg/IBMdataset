N=int(input())
A=[-1]+[int(i)-1 for i in input().split()]
P=[[] for i in range(N)]
for i in range(1,N):
    P[A[i]].append(i)
for i in range(N):
    print(len(P[i]))