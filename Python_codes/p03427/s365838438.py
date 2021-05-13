x=int(input())
y=str(x)
n=len(y)

if y[1:]=="9"*(n-1):
    print(int(y[0])+9*n-9)
else:
    print(int(y[0])-1+9*n-9)
