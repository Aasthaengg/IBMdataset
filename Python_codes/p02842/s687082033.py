N=int(input())
X=int(N//1.08)
n1=int(X*1.08)
n2=int((X+1)*1.08)
if n1==N:
    print(X)
elif n2==N:
    print(X+1)
else:
    print(':(')
