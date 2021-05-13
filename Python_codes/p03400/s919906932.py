N=int(input())
D,X=map(int,input().split())
A=[]
for _ in range(N):
    A.append(int(input()))

sum = 0
for i in range(N):
    a = A[i]
    sum += ((D - 1) // a) + 1

print(sum + X)