A,B=list(map(str,input().split()))
a=int(A)
b=int(B[:-3]+B[-2:])
print(a*b//100)