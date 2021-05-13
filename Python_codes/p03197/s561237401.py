N=int(input())
A=[]
flag=False
for i in range(N):
    A.append(int(input()))
    if A[i]%2==1:
        flag=True

if not flag:
    print("second")
else:
    print("first")