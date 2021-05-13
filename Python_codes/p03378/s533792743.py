N,M,X=map(int,input().split())
L=list(map(int,input().split()))
K=[i for i in L if i>X]
T=[i for i in L if i<X]
print(min(len(K),len(T)))