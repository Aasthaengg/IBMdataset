n=int(input())
a=list(map(int,input().split()))

A=sorted(a)

m1=A[n//2 -1]
m2=A[n//2]
for i in range(n):
    if a[i]<=m1:
        print(m2)
    else:
        print(m1)