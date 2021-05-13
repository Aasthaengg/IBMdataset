n=int(input())
A=[]
B=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if n%2==0:
    a_min=(A[n//2-1]+A[n//2])/2
    b_max=(B[n//2-1]+B[n//2])/2
    print(int(1+(b_max-a_min)/0.5))
else:
    a_min=A[n//2]
    b_max=B[n//2]
    print(int(b_max-a_min)+1)