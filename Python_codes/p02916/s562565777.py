input()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

m=0
y=-1
for x in A:
    m+=B[x-1]
    if x==y+1:
        m+=C[y-1]
    y=x
print(m)