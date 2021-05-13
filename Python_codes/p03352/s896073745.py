import math
X=int(input())
x=int((X**(1/2))//1)
A=[]
y=int(math.log2(X)//1)
for i in range(x+1):
    for j in range(y+1):
        if i**j<=X:
            A.append(i**j)
print(max(A))