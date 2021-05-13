A1,A2,A3=map(int,input().split())

A=[A1,A2,A3]

B=sorted(A)

print(B[1]-B[0]+B[2]-B[1])