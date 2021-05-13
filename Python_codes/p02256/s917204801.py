A = list(map(int,input().split()))
a=A[0]
b=A[1]
while b:
    a,b=b,a%b
print(a)