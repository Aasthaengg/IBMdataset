# coding: utf-8
A,B=input().split()
A=int(A)
B=int(B.replace('.',""))
ans=A*B
ans=ans//100

print(ans)