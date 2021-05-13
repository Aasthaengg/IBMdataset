
X=input()

N=len(X)
n=N-1
A=0
num=0
total=0

for i in range(2**n):
    A=X[0]
    for j in range(n):
        if (i>>j)&1:
            A+=".+"+X[j+1]
        else:
            A+=".-"+X[j+1]

    num=list(map(int,A.split(".")))
    total=sum(num)

    if total==7:
        break

print(A.replace(".","")+"=7")
