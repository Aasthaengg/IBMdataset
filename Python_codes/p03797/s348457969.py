a,b=map(int,input().split())
A=min(a,b//2)
a-=A
b-=A*2
A+=b//4
print(A)