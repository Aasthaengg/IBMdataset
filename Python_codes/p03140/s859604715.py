N=int(input())
A=input()
B=input()
C=input()

num=0
for i in range(N):
    str=[]
    str.append(A[i])
    str.append(B[i])
    str.append(C[i])
    num=num+len(set(str))-1
print(num)