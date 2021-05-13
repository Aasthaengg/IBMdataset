I=input
N,A=I(),list(map(int,I().split()))
A.sort()
print(sum(A[-1::-2])-sum(A[-2::-2]))