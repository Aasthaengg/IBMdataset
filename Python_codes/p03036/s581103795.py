r,D,x=map(int,input().split())
A=[]


for i in range(1,11):
    B=r*x-D
    A.append(B)
    x=B
for s in A:
    print(s)