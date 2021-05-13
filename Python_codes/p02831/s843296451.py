A=list(map(int,input().split()))
x=max(A)
n=min(A)
while(n!=0):
    x,n=n,x%n
print(int(max(A)*min(A)/x))