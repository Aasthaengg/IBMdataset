N=int(input())
A=input()
B=input()
C=input()

print(sum([len(set([A[i],B[i],C[i]]))-1 for i in range(N)]))