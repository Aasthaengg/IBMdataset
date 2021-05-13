N = int(input())
A = [int(i) for i in input().split()]

A.reverse()
ans = []

for i in range(0,N,2):
    ans.append(A[i])

A.reverse()

for i in range(N%2,N,2):
    ans.append(A[i])

[print(i,end=' ') for i in ans]
