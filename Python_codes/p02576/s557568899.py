N,X,T = [int(i) for i in input().split()]
print(T*(N//X + 1 - (X - (N%X))//X ))