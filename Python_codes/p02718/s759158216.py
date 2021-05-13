n,m=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(A,reverse=True)
sum=0
for i in range(n):
    sum+=B[i]
if 4*m*B[m-1]<sum:
    print("No")
else:
    print("Yes")