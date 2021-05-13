N=int(input())
A = list(map(int,input().split()))
Q=int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i]=map(int,input().split())
#print(B,C)
#print(A)
#a = 0
#for i in range(N):
    #a += A[i]
#print(a)
ls = [0]*100000
for i in A:
    ls[i-1] += 1
#print(ls)
sumA = sum(A)
#print("sumA",sumA)
for j in range(Q):
    #print(B[j]-1)
    #print(ls)
    sumA += (C[j]-B[j])*ls[B[j]-1]
    #print("j","C[j]","B[j]","ls[B[j]]",j,C[j],B[j],ls[B[j]-1])
    ls[C[j]-1] += ls[B[j]-1]
    ls[B[j]-1] = 0
    print(sumA)
