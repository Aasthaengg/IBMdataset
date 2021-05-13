n=int(input())
A=[]
a=0
i=0
while a*2 <= n:
    a = 2**i
    A.append(a)
    i=i+1
print(A[-1])