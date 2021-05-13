n = int(input())
A=[]
B=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if n%2==0:
    A_med=(A[int(n/2)-1]+A[int(n/2)])/2
    B_med=(B[int(n/2)-1]+B[int(n/2)])/2
    print(int((B_med-A_med)*2+1))
else:
    A_med=A[int((n+1)/2)-1]
    B_med=B[int((n+1)/2)-1]
    print(int(B_med-A_med+1))