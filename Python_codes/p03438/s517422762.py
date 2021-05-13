N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))


K=sum(B)-sum(A) #操作の回数はK回で確定

# b[j]に+1をa[j]に-1に変換する
Plus_Two=K
Minus_One=K


for i in range(N):
    D=B[i]-A[i]
    if D>0:
        Plus_Two-=(D+1)//2
        Minus_One-=D%2
    else:
        D=-D
        Minus_One-=D

if min(Plus_Two,Minus_One)>=0:
    print("Yes")
else:
    print("No")
