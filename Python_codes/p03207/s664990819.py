N = int(input())
A=[]
for i in range(N):
    A += [int(input())]

A.sort()
print(sum(A) - A[N-1]//2)