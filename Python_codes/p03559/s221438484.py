n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
B.sort()
C.sort()


Bnum=[]
a=0
for i in range(n):
    while a!=n and B[i]>A[a] :
        a+=1
    Bnum.append(a)

Cnum=[]
b=0
s=0
for i in range(n):
    while b!=n and C[i]>B[b]:
        s+=Bnum[b]
        b+=1
    Cnum.append(s)

print(sum(Cnum))