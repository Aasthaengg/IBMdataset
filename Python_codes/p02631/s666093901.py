n=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(0,n,2):
    B.append(A[i]^A[i+1])

s=0
for b in B:
    s^=b

X=[s^a for a in A]
print(*X)