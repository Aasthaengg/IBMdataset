N=int(input())
A=list(map(int,input().split()))

X=[0]*8
Y=0

for a in A:
    if a>=3200:
        Y+=1
    else:
        X[a//400]+=1

a=max(1,8-X.count(0))
b=8-X.count(0)+Y
print(a,b)
