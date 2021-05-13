a,b=map(int,input().split())
A=[]
for i in range(1,1000):
    A.append((i*(i+1))//2)

for j in range(5*(10**6)):
    if ((a+j) in A) and ((b+j) in A):
        if A.index(a+j)+1==A.index(b+j):
            print(j)
            exit()